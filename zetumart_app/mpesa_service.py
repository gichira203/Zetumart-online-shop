import requests
import base64
from datetime import datetime
from django.conf import settings
from django.utils import timezone
from .models import Order, PaymentTransaction
import json
import logging

logger = logging.getLogger(__name__)

class MpesaService:
    def __init__(self):
        self.consumer_key = settings.MPESA_CONSUMER_KEY
        self.consumer_secret = settings.MPESA_CONSUMER_SECRET
        self.passkey = settings.MPESA_PASSKEY
        self.business_shortcode = settings.MPESA_BUSINESS_SHORTCODE
        self.callback_url = settings.MPESA_CALLBACK_URL
        self.base_url = "https://sandbox.safaricom.co.ke" if settings.DEBUG else "https://api.safaricom.co.ke"
        self.access_token = None
        self.token_expires_at = None
        
        # Validate callback URL
        if not self.callback_url or self.callback_url == 'https://webhook.site/your-unique-id':
            logger.warning("M-Pesa callback URL is not configured properly. Please update MPESA_CALLBACK_URL in settings.")

    def get_access_token(self):
        """Get OAuth access token from M-Pesa API"""
        if self.access_token and self.token_expires_at and timezone.now() < self.token_expires_at:
            return self.access_token

        url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
        try:
            # Debug logging
            logger.info(f"M-Pesa OAuth Request URL: {url}")
            logger.info(f"M-Pesa Consumer Key: {self.consumer_key[:20]}...")
            logger.info(f"M-Pesa Consumer Secret: {self.consumer_secret[:20]}...")
            logger.info(f"M-Pesa Base URL: {self.base_url}")
            
            # Create basic auth header
            auth_string = f"{self.consumer_key}:{self.consumer_secret}"
            logger.info(f"M-Pesa Auth String (first 20 chars): {auth_string[:20]}...")
            
            auth_bytes = auth_string.encode('ascii')
            auth_b64 = base64.b64encode(auth_bytes).decode('ascii')
            logger.info(f"M-Pesa Base64 Auth (first 20 chars): {auth_b64[:20]}...")
            
            headers = {
                'Authorization': f'Basic {auth_b64}',
                'Content-Type': 'application/json'
            }
            
            logger.info(f"M-Pesa Request Headers: {headers}")
            
            response = requests.get(url, headers=headers, timeout=30)
            
            logger.info(f"M-Pesa OAuth Response Status: {response.status_code}")
            logger.info(f"M-Pesa OAuth Response Headers: {dict(response.headers)}")
            logger.info(f"M-Pesa OAuth Response Body: {response.text}")
            
            response.raise_for_status()
            
            data = response.json()
            self.access_token = data['access_token']
            # Token expires in 1 hour (3600 seconds)
            self.token_expires_at = timezone.now() + timezone.timedelta(seconds=3500)
            
            return self.access_token
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting M-Pesa access token: {str(e)}")
            raise Exception(f"Failed to get M-Pesa access token: {str(e)}")

    def stk_push_request(self, phone_number, amount, order_id, account_reference=None):
        """Initiate M-Pesa STK Push payment"""
        try:
            access_token = self.get_access_token()
            url = f"{self.base_url}/mpesa/stkpush/v1/processrequest"
            
            # Format phone number (remove +254 if present and ensure it starts with 254)
            if phone_number.startswith('+'):
                phone_number = phone_number[1:]
            if not phone_number.startswith('254'):
                if phone_number.startswith('0'):
                    phone_number = '254' + phone_number[1:]
                elif phone_number.startswith('07'):
                    phone_number = '254' + phone_number[2:]
                elif phone_number.startswith('01'):
                    phone_number = '254' + phone_number[2:]
                elif phone_number.startswith('7') and len(phone_number) > 9:  # Handle case like 07657/0111383
                    phone_number = '254' + phone_number
                elif phone_number.startswith('1') and len(phone_number) > 9:  # Handle case like 0111383/07657
                    phone_number = '254' + phone_number
                else:
                    phone_number = '254' + phone_number
            
            # Convert amount to integer properly
            try:
                amount_int = int(float(amount))
            except (ValueError, TypeError):
                return {
                    'success': False,
                    'error': f'Invalid amount format: {amount}'
                }
            
            # Generate timestamp
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            
            # Generate password
            password_str = f"{self.business_shortcode}{self.passkey}{timestamp}"
            password_bytes = password_str.encode('ascii')
            password = base64.b64encode(password_bytes).decode('ascii')
            
            # Prepare request payload
            payload = {
                "BusinessShortCode": self.business_shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount_int,
                "PartyA": phone_number,
                "PartyB": self.business_shortcode,
                "PhoneNumber": phone_number,
                "CallBackURL": self.callback_url,
                "AccountReference": account_reference or order_id,
                "TransactionDesc": f"Payment for Order {order_id}"
            }
            
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            
            response = requests.post(url, json=payload, headers=headers)
            
            # Log the full request and response for debugging
            logger.info(f"M-Pesa STK Push Request URL: {url}")
            logger.info(f"M-Pesa STK Push Payload: {json.dumps(payload, indent=2)}")
            logger.info(f"M-Pesa STK Push Response Status: {response.status_code}")
            logger.info(f"M-Pesa STK Push Response Body: {response.text}")
            
            response.raise_for_status()
            
            data = response.json()
            
            # Create payment transaction record
            transaction = PaymentTransaction.objects.create(
                order=Order.objects.get(order_id=order_id),
                transaction_type='stk_push',
                transaction_id=data.get('CheckoutRequestID', ''),
                merchant_request_id=data.get('MerchantRequestID', ''),
                checkout_request_id=data.get('CheckoutRequestID', ''),
                phone_number=phone_number,
                amount=amount_int,
                status='pending',
                response_data=data
            )
            
            return {
                'success': True,
                'transaction_id': transaction.id,
                'checkout_request_id': data.get('CheckoutRequestID'),
                'merchant_request_id': data.get('MerchantRequestID'),
                'response_desc': data.get('ResponseDescription', '')
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"STK Push request failed: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
        except Exception as e:
            logger.error(f"STK Push error: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }

    def transaction_status_query(self, checkout_request_id):
        """Query the status of an STK Push transaction"""
        try:
            access_token = self.get_access_token()
            url = f"{self.base_url}/mpesa/stkpushquery/v1/query"
            
            # Generate timestamp
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            
            # Generate password
            password_str = f"{self.business_shortcode}{self.passkey}{timestamp}"
            password_bytes = password_str.encode('ascii')
            password = base64.b64encode(password_bytes).decode('ascii')
            
            payload = {
                "BusinessShortCode": self.business_shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "CheckoutRequestID": checkout_request_id
            }
            
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            return data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Transaction status query failed: {str(e)}")
            raise Exception(f"Failed to query transaction status: {str(e)}")

    def verify_transaction_code(self, transaction_code, amount, phone_number):
        """Verify a transaction code using M-Pesa Transaction Status API"""
        try:
            access_token = self.get_access_token()
            url = f"{self.base_url}/mpesa/transactionstatus/v1/query"
            
            # Format phone number
            if phone_number.startswith('+'):
                phone_number = phone_number[1:]
            if not phone_number.startswith('254'):
                if phone_number.startswith('0'):
                    phone_number = '254' + phone_number[1:]
                else:
                    phone_number = '254' + phone_number
            
            # Generate timestamp
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            
            # Generate password for transaction status
            password_str = f"{self.business_shortcode}{self.passkey}{timestamp}"
            password_bytes = password_str.encode('ascii')
            password = base64.b64encode(password_bytes).decode('ascii')
            
            payload = {
                "Initiator": "apiuser",  # This should be configured in your M-Pesa portal
                "SecurityCredential": "your_security_credential",  # This should be configured
                "CommandID": "TransactionStatusQuery",
                "TransactionID": transaction_code,
                "PartyA": phone_number,
                "IdentifierType": "1",  # 1 = MSISDN (phone number)
                "ResultURL": self.callback_url,
                "QueueTimeOutURL": self.callback_url,
                "Remarks": f"Verify transaction {transaction_code}",
                "Occasion": ""
            }
            
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            
            # Check if transaction is valid and matches amount
            if data.get('ResultCode') == '0':
                transaction_amount = float(data.get('ResultParameters', {}).get('TransactionAmount', 0))
                if abs(transaction_amount - amount) < 0.01:  # Allow small floating point differences
                    return {
                        'valid': True,
                        'amount': transaction_amount,
                        'transaction_date': data.get('ResultParameters', {}).get('TransactionCompletedDateTime'),
                        'receipt_number': transaction_code
                    }
            
            return {
                'valid': False,
                'error': 'Transaction not found or amount mismatch'
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Transaction verification failed: {str(e)}")
            return {
                'valid': False,
                'error': str(e)
            }

    def process_callback(self, callback_data):
        """Process M-Pesa callback data"""
        try:
            # Extract data from callback
            stk_callback = callback_data.get('Body', {}).get('stkCallback', {})
            merchant_request_id = stk_callback.get('MerchantRequestID')
            checkout_request_id = stk_callback.get('CheckoutRequestID')
            result_code = stk_callback.get('ResultCode')
            result_desc = stk_callback.get('ResultDesc')
            
            # Find the transaction
            transaction = PaymentTransaction.objects.filter(
                checkout_request_id=checkout_request_id
            ).first()
            
            if not transaction:
                logger.error(f"Transaction not found for CheckoutRequestID: {checkout_request_id}")
                return {'success': False, 'error': 'Transaction not found'}
            
            # Update transaction based on result
            if result_code == '0':  # Success
                # Extract payment details
                callback_metadata = stk_callback.get('CallbackMetadata', {}).get('Item', [])
                amount = 0
                phone_number = ''
                receipt_number = ''
                transaction_date = None
                
                for item in callback_metadata:
                    name = item.get('Name')
                    value = item.get('Value')
                    
                    if name == 'Amount':
                        amount = float(value)
                    elif name == 'PhoneNumber':
                        phone_number = value
                    elif name == 'MpesaReceiptNumber':
                        receipt_number = value
                    elif name == 'TransactionDate':
                        # Convert timestamp to datetime
                        timestamp_str = str(value)
                        if len(timestamp_str) == 14:
                            transaction_date = datetime.strptime(timestamp_str, '%Y%m%d%H%M%S')
                
                # Update transaction
                transaction.status = 'completed'
                transaction.result_code = result_code
                transaction.result_desc = result_desc
                transaction.receipt_number = receipt_number
                transaction.transaction_date = transaction_date
                transaction.response_data = callback_data
                transaction.save()
                
                # Update order
                order = transaction.order
                order.payment_status = 'completed'
                order.order_status = 'paid'
                order.save()
                
                # Create order tracking
                from .models import OrderTracking
                OrderTracking.objects.create(
                    order=order,
                    status='Payment Confirmed',
                    description=f'Payment of KES {amount} confirmed via M-Pesa. Receipt: {receipt_number}',
                    location='M-Pesa System'
                )
                
                return {
                    'success': True,
                    'status': 'completed',
                    'receipt_number': receipt_number,
                    'amount': amount
                }
                
            else:  # Failed or cancelled
                transaction.status = 'failed' if result_code != '1032' else 'cancelled'
                transaction.result_code = result_code
                transaction.result_desc = result_desc
                transaction.response_data = callback_data
                transaction.save()
                
                # Update order
                order = transaction.order
                order.payment_status = 'failed'
                order.order_status = 'cancelled' if result_code == '1032' else 'failed'
                order.save()
                
                # Create order tracking
                from .models import OrderTracking
                OrderTracking.objects.create(
                    order=order,
                    status='Payment Failed',
                    description=f'Payment failed: {result_desc}',
                    location='M-Pesa System'
                )
                
                return {
                    'success': False,
                    'status': 'failed' if result_code != '1032' else 'cancelled',
                    'error': result_desc
                }
                
        except Exception as e:
            logger.error(f"Error processing M-Pesa callback: {str(e)}")
            return {'success': False, 'error': str(e)}
