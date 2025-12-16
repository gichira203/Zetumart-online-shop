import requests
import json
import hashlib
import hmac
import base64
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse
from .models import Order

class MpesaPaymentService:
    """M-Pesa payment integration service"""
    
    def __init__(self):
        self.consumer_key = getattr(settings, 'MPESA_CONSUMER_KEY', '')
        self.consumer_secret = getattr(settings, 'MPESA_CONSUMER_SECRET', '')
        self.passkey = getattr(settings, 'MPESA_PASSKEY', '')
        self.business_shortcode = getattr(settings, 'MPESA_BUSINESS_SHORTCODE', '174379')
        self.base_url = 'https://api.safaricom.co.ke'
        self.callback_url = getattr(settings, 'MPESA_CALLBACK_URL', 'https://yourdomain.com/api/mpesa/callback/')
        
    def get_access_token(self):
        """Get M-Pesa API access token"""
        try:
            api_url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
            response = requests.get(
                api_url,
                auth=(self.consumer_key, self.consumer_secret)
            )
            
            if response.status_code == 200:
                return response.json().get('access_token')
            else:
                return None
        except Exception as e:
            print(f"M-Pesa token error: {e}")
            return None
    
    def initiate_stk_push(self, phone_number, amount, order_id, account_reference=None):
        """Initiate M-Pesa STK Push payment"""
        try:
            access_token = self.get_access_token()
            if not access_token:
                return {'success': False, 'error': 'Failed to get access token'}
            
            # Format phone number (remove +254 if present, ensure starts with 254)
            if phone_number.startswith('+254'):
                phone_number = phone_number.replace('+254', '254')
            elif phone_number.startswith('07'):
                phone_number = phone_number.replace('07', '2547')
            elif phone_number.startswith('01'):
                phone_number = phone_number.replace('01', '2541')
            
            # Generate password
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            password_string = f"{self.business_shortcode}{self.passkey}{timestamp}"
            password = base64.b64encode(password_string.encode()).decode()
            
            # Prepare STK push request
            api_url = f"{self.base_url}/mpesa/stkpush/v1/processrequest"
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'BusinessShortCode': self.business_shortcode,
                'Password': password,
                'Timestamp': timestamp,
                'TransactionType': 'CustomerPayBillOnline',
                'Amount': int(amount),
                'PartyA': phone_number,
                'PartyB': self.business_shortcode,
                'PhoneNumber': phone_number,
                'CallBackURL': f"{self.callback_url}?order_id={order_id}",
                'AccountReference': account_reference or f"ZM{order_id}",
                'TransactionDesc': f"Payment for order {order_id}"
            }
            
            response = requests.post(api_url, json=payload, headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('ResponseCode') == '0':
                    return {
                        'success': True,
                        'checkout_request_id': result.get('CheckoutRequestID'),
                        'merchant_request_id': result.get('MerchantRequestID'),
                        'customer_message': result.get('CustomerMessage')
                    }
                else:
                    return {
                        'success': False,
                        'error': result.get('errorMessage', 'STK push failed')
                    }
            else:
                return {
                    'success': False,
                    'error': f'HTTP {response.status_code}: {response.text}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def check_payment_status(self, checkout_request_id):
        """Check M-Pesa payment status"""
        try:
            access_token = self.get_access_token()
            if not access_token:
                return {'success': False, 'error': 'Failed to get access token'}
            
            api_url = f"{self.base_url}/mpesa/stkpushquery/v1/query"
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            password_string = f"{self.business_shortcode}{self.passkey}{timestamp}"
            password = base64.b64encode(password_string.encode()).decode()
            
            payload = {
                'BusinessShortCode': self.business_shortcode,
                'Password': password,
                'Timestamp': timestamp,
                'CheckoutRequestID': checkout_request_id
            }
            
            response = requests.post(api_url, json=payload, headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                return {
                    'success': True,
                    'status': result.get('ResultCode'),
                    'message': result.get('ResultDesc'),
                    'data': result
                }
            else:
                return {
                    'success': False,
                    'error': f'HTTP {response.status_code}: {response.text}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

class PayPalPaymentService:
    """PayPal payment integration service"""
    
    def __init__(self):
        self.client_id = getattr(settings, 'PAYPAL_CLIENT_ID', '')
        self.client_secret = getattr(settings, 'PAYPAL_CLIENT_SECRET', '')
        self.base_url = 'https://api-m.sandbox.paypal.com'  # Use sandbox for testing
        self.return_url = getattr(settings, 'PAYPAL_RETURN_URL', 'https://yourdomain.com/payment/success/')
        self.cancel_url = getattr(settings, 'PAYPAL_CANCEL_URL', 'https://yourdomain.com/payment/cancel/')
        
    def get_access_token(self):
        """Get PayPal API access token"""
        try:
            auth_string = f"{self.client_id}:{self.client_secret}"
            encoded_auth = base64.b64encode(auth_string.encode()).decode()
            
            headers = {
                'Authorization': f'Basic {encoded_auth}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            data = 'grant_type=client_credentials'
            response = requests.post(f"{self.base_url}/v1/oauth2/token", 
                                   headers=headers, data=data)
            
            if response.status_code == 200:
                return response.json().get('access_token')
            else:
                return None
        except Exception as e:
            print(f"PayPal token error: {e}")
            return None
    
    def create_payment(self, amount, order_id, return_url=None, cancel_url=None):
        """Create PayPal payment"""
        try:
            access_token = self.get_access_token()
            if not access_token:
                return {'success': False, 'error': 'Failed to get access token'}
            
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            
            payment_data = {
                'intent': 'sale',
                'payer': {
                    'payment_method': 'paypal'
                },
                'transactions': [{
                    'amount': {
                        'total': str(amount),
                        'currency': 'USD'
                    },
                    'description': f'Payment for order {order_id}',
                    'custom': str(order_id)
                }],
                'redirect_urls': {
                    'return_url': return_url or self.return_url,
                    'cancel_url': cancel_url or self.cancel_url
                }
            }
            
            response = requests.post(f"{self.base_url}/v1/payments/payment", 
                                   json=payment_data, headers=headers)
            
            if response.status_code == 201:
                result = response.json()
                approval_url = None
                for link in result.get('links', []):
                    if link.get('rel') == 'approval_url':
                        approval_url = link.get('href')
                        break
                
                return {
                    'success': True,
                    'payment_id': result.get('id'),
                    'approval_url': approval_url
                }
            else:
                return {
                    'success': False,
                    'error': f'HTTP {response.status_code}: {response.text}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def execute_payment(self, payment_id, payer_id):
        """Execute PayPal payment"""
        try:
            access_token = self.get_access_token()
            if not access_token:
                return {'success': False, 'error': 'Failed to get access token'}
            
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            
            payment_data = {
                'payer_id': payer_id
            }
            
            response = requests.post(f"{self.base_url}/v1/payments/payment/{payment_id}/execute", 
                                   json=payment_data, headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('state') == 'approved':
                    return {
                        'success': True,
                        'transaction_id': result.get('transactions')[0].get('related_resources')[0].get('sale').get('id')
                    }
                else:
                    return {
                        'success': False,
                        'error': 'Payment not approved'
                    }
            else:
                return {
                    'success': False,
                    'error': f'HTTP {response.status_code}: {response.text}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

class CardPaymentService:
    """Card payment processing service (Stripe-like implementation)"""
    
    def __init__(self):
        self.secret_key = getattr(settings, 'CARD_PAYMENT_SECRET_KEY', '')
        self.publishable_key = getattr(settings, 'CARD_PAYMENT_PUBLISHABLE_KEY', '')
        self.base_url = 'https://api.stripe.com/v1'  # Using Stripe as example
        
    def create_payment_intent(self, amount, order_id, currency='KES'):
        """Create payment intent for card payment"""
        try:
            headers = {
                'Authorization': f'Bearer {self.secret_key}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            data = {
                'amount': int(amount * 100),  # Convert to cents
                'currency': currency.lower(),
                'metadata': {'order_id': str(order_id)},
                'payment_method_types': ['card']
            }
            
            response = requests.post(f"{self.base_url}/payment_intents", 
                                   headers=headers, data=data)
            
            if response.status_code == 200:
                result = response.json()
                return {
                    'success': True,
                    'client_secret': result.get('client_secret'),
                    'payment_intent_id': result.get('id')
                }
            else:
                return {
                    'success': False,
                    'error': f'HTTP {response.status_code}: {response.text}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def confirm_payment(self, payment_intent_id):
        """Confirm card payment"""
        try:
            headers = {
                'Authorization': f'Bearer {self.secret_key}',
                'Content-Type': 'application/json'
            }
            
            response = requests.get(f"{self.base_url}/payment_intents/{payment_intent_id}", 
                                  headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                return {
                    'success': result.get('status') == 'succeeded',
                    'status': result.get('status'),
                    'amount': result.get('amount'),
                    'currency': result.get('currency'),
                    'payment_method': result.get('payment_method')
                }
            else:
                return {
                    'success': False,
                    'error': f'HTTP {response.status_code}: {response.text}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

class PaymentProcessor:
    """Main payment processor that handles all payment methods"""
    
    def __init__(self):
        self.mpesa_service = MpesaPaymentService()
        self.paypal_service = PayPalPaymentService()
        self.card_service = CardPaymentService()
    
    def process_payment(self, payment_method, payment_data, order_id, amount):
        """Process payment based on method"""
        
        if payment_method == 'mpesa':
            return self.mpesa_service.initiate_stk_push(
                phone_number=payment_data.get('phone'),
                amount=amount,
                order_id=order_id,
                account_reference=f"ZM{order_id}"
            )
            
        elif payment_method == 'paypal':
            return self.paypal_service.create_payment(
                amount=amount,
                order_id=order_id,
                return_url=f"/payment/success/?order_id={order_id}",
                cancel_url=f"/payment/cancel/?order_id={order_id}"
            )
            
        elif payment_method == 'card':
            return self.card_service.create_payment_intent(
                amount=amount,
                order_id=order_id
            )
            
        elif payment_method == 'till':
            # For till payments, we just validate and record
            transaction_code = payment_data.get('transaction_code')
            if not transaction_code:
                return {'success': False, 'error': 'Transaction code is required'}
            
            return {
                'success': True,
                'message': 'Transaction recorded. Awaiting verification.',
                'transaction_code': transaction_code
            }
            
        elif payment_method == 'polepole':
            # For Lipa Mdogo Mdogo, calculate installment plan
            installment_plan = payment_data.get('installment_plan', '3months')
            upfront_payment = amount * 0.3
            
            return {
                'success': True,
                'message': 'Installment plan created',
                'upfront_payment': upfront_payment,
                'installment_plan': installment_plan,
                'monthly_payment': (amount * 0.7) / int(installment_plan.replace('months', ''))
            }
            
        elif payment_method == 'cod':
            # Pay on Delivery - no payment processing needed
            return {
                'success': True,
                'message': 'Pay on Delivery selected'
            }
            
        else:
            return {'success': False, 'error': 'Invalid payment method'}
    
    def verify_payment(self, payment_method, verification_data):
        """Verify payment completion"""
        
        if payment_method == 'mpesa':
            checkout_request_id = verification_data.get('checkout_request_id')
            if not checkout_request_id:
                return {'success': False, 'error': 'Checkout request ID required'}
            
            return self.mpesa_service.check_payment_status(checkout_request_id)
            
        elif payment_method == 'paypal':
            payment_id = verification_data.get('payment_id')
            payer_id = verification_data.get('payer_id')
            
            if not payment_id or not payer_id:
                return {'success': False, 'error': 'Payment ID and Payer ID required'}
            
            return self.paypal_service.execute_payment(payment_id, payer_id)
            
        elif payment_method == 'card':
            payment_intent_id = verification_data.get('payment_intent_id')
            if not payment_intent_id:
                return {'success': False, 'error': 'Payment intent ID required'}
            
            return self.card_service.confirm_payment(payment_intent_id)
            
        elif payment_method == 'till':
            # For till payments, verify transaction code format
            transaction_code = verification_data.get('transaction_code')
            if not transaction_code or len(transaction_code) < 6:
                return {'success': False, 'error': 'Invalid transaction code'}
            
            return {'success': True, 'message': 'Transaction code verified'}
            
        else:
            return {'success': True, 'message': 'Payment verified'}
