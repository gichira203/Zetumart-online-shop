import json
import logging
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Order, Notification, UserProfile
import requests

logger = logging.getLogger(__name__)

class NotificationService:
    """Centralized notification service for ZetuMart"""
    
    def __init__(self):
        self.site_name = getattr(settings, 'SITE_NAME', 'ZetuMart')
        self.admin_email = getattr(settings, 'ADMIN_EMAIL', 'admin@zetumart.co.ke')
        self.site_url = getattr(settings, 'SITE_URL', 'https://yourdomain.com')
    
    def send_order_notification(self, order, notification_type, additional_data=None):
        """Send order-related notifications via multiple channels"""
        
        notification_methods = {
            'email': self._send_email_notification,
            'database': self._create_database_notification,
            'sms': self._send_sms_notification,
            'whatsapp': self._send_whatsapp_notification,
            'push': self._send_push_notification
        }
        
        # Get notification content
        content = self._get_notification_content(order, notification_type, additional_data)
        
        # Determine which channels to use based on type and user preferences
        channels = self._get_notification_channels(notification_type, order)
        
        # Send notifications through each channel
        results = {}
        for channel in channels:
            if channel in notification_methods:
                try:
                    result = notification_methods[channel](order, content, notification_type)
                    results[channel] = result
                except Exception as e:
                    logger.error(f"Failed to send {channel} notification: {e}")
                    results[channel] = {'success': False, 'error': str(e)}
        
        return results
    
    def _get_notification_content(self, order, notification_type, additional_data=None):
        """Get notification content based on type"""
        
        base_data = {
            'order_id': order.order_id,
            'customer_name': order.customer_name,
            'customer_email': order.customer_email,
            'customer_phone': order.customer_phone,
            'total_amount': order.total_amount,
            'delivery_county': order.delivery_county,
            'delivery_town': order.delivery_town,
            'payment_method': order.get_payment_method_display(),
            'site_name': self.site_name,
            'site_url': self.site_url
        }
        
        if additional_data:
            base_data.update(additional_data)
        
        contents = {
            'order_created': {
                'subject': f'Order Confirmation - {order.order_id}',
                'title': f'Order {order.order_id} Confirmed',
                'message': f'Thank you for your order! Your order #{order.order_id} has been confirmed and is being processed.',
                'template': 'emails/order_confirmation.html',
                'sms_message': f'Your order {order.order_id} has been confirmed. Total: KSh {order.total_amount}. We\'ll notify you when it ships.'
            },
            'payment_received': {
                'subject': f'Payment Received - {order.order_id}',
                'title': f'Payment Received for Order {order.order_id}',
                'message': f'We have received your payment for order #{order.order_id}. Your order is now being processed.',
                'template': 'emails/payment_received.html',
                'sms_message': f'Payment received for order {order.order_id}. Your order is now being processed.'
            },
            'order_shipped': {
                'subject': f'Order Shipped - {order.order_id}',
                'title': f'Your Order {order.order_id} Has Been Shipped',
                'message': f'Great news! Your order #{order.order_id} has been shipped and is on its way to you.',
                'template': 'emails/order_shipped.html',
                'sms_message': f'Your order {order.order_id} has been shipped! Track it at {self.site_url}/order-tracking/{order.order_id}/'
            },
            'order_delivered': {
                'subject': f'Order Delivered - {order.order_id}',
                'title': f'Your Order {order.order_id} Has Been Delivered',
                'message': f'Your order #{order.order_id} has been delivered successfully. Thank you for shopping with {self.site_name}!',
                'template': 'emails/order_delivered.html',
                'sms_message': f'Your order {order.order_id} has been delivered. Thank you for shopping with {self.site_name}!'
            },
            'payment_failed': {
                'subject': f'Payment Failed - {order.order_id}',
                'title': f'Payment Failed for Order {order.order_id}',
                'message': f'We were unable to process your payment for order #{order.order_id}. Please update your payment information.',
                'template': 'emails/payment_failed.html',
                'sms_message': f'Payment failed for order {order.order_id}. Please update your payment method to continue.'
            },
            'order_cancelled': {
                'subject': f'Order Cancelled - {order.order_id}',
                'title': f'Order {order.order_id} Cancelled',
                'message': f'Your order #{order.order_id} has been cancelled as requested.',
                'template': 'emails/order_cancelled.html',
                'sms_message': f'Your order {order.order_id} has been cancelled. Refund will be processed if applicable.'
            }
        }
        
        content = contents.get(notification_type, contents['order_created'])
        content.update(base_data)
        
        return content
    
    def _get_notification_channels(self, notification_type, order):
        """Determine which notification channels to use"""
        
        # Default channels for all notifications
        channels = ['database']
        
        # Always send email for important order updates
        if notification_type in ['order_created', 'payment_received', 'order_shipped', 'order_delivered']:
            channels.append('email')
        
        # Send SMS for critical updates
        if notification_type in ['order_shipped', 'payment_failed']:
            channels.append('sms')
        
        # Send WhatsApp for delivery updates (if configured)
        if notification_type == 'order_delivered' and getattr(settings, 'WHATSAPP_API_TOKEN', None):
            channels.append('whatsapp')
        
        return channels
    
    def _send_email_notification(self, order, content, notification_type):
        """Send email notification"""
        
        try:
            # Render email template
            html_content = render_to_string(content.get('template', 'emails/base_notification.html'), content)
            
            # Send email
            send_mail(
                subject=content['subject'],
                message=content['message'],  # Plain text version
                from_email=f'{self.site_name} <noreply@zetumart.co.ke>',
                recipient_list=[order.customer_email],
                html_message=html_content,
                fail_silently=False
            )
            
            logger.info(f"Email notification sent for order {order.order_id}")
            return {'success': True, 'channel': 'email'}
            
        except Exception as e:
            logger.error(f"Failed to send email notification: {e}")
            return {'success': False, 'error': str(e), 'channel': 'email'}
    
    def _create_database_notification(self, order, content, notification_type):
        """Create database notification for user dashboard"""
        
        try:
            # Create notification record
            notification = Notification.objects.create(
                user=order.user if order.user else None,
                title=content['title'],
                message=content['message'],
                notification_type=notification_type,
                related_order_id=order.order_id,
                is_read=False
            )
            
            logger.info(f"Database notification created for order {order.order_id}")
            return {'success': True, 'channel': 'database', 'notification_id': notification.id}
            
        except Exception as e:
            logger.error(f"Failed to create database notification: {e}")
            return {'success': False, 'error': str(e), 'channel': 'database'}
    
    def _send_sms_notification(self, order, content, notification_type):
        """Send SMS notification"""
        
        try:
            # This would integrate with an SMS service like Twilio, Africa's Talking, etc.
            # For now, we'll just log it
            
            sms_message = content.get('sms_message', content['message'])
            phone_number = order.customer_phone
            
            # Example SMS integration (commented out - would need actual SMS service)
            """
            from twilio.rest import Client
            
            account_sid = settings.TWILIO_ACCOUNT_SID
            auth_token = settings.TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)
            
            message = client.messages.create(
                body=sms_message,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=phone_number
            )
            """
            
            logger.info(f"SMS notification would be sent to {phone_number}: {sms_message}")
            return {'success': True, 'channel': 'sms', 'message': 'SMS logged (integration needed)'}
            
        except Exception as e:
            logger.error(f"Failed to send SMS notification: {e}")
            return {'success': False, 'error': str(e), 'channel': 'sms'}
    
    def _send_whatsapp_notification(self, order, content, notification_type):
        """Send WhatsApp notification"""
        
        try:
            # This would integrate with WhatsApp Business API
            whatsapp_number = getattr(settings, 'WHATSAPP_BUSINESS_NUMBER', None)
            api_token = getattr(settings, 'WHATSAPP_API_TOKEN', None)
            
            if not whatsapp_number or not api_token:
                return {'success': False, 'error': 'WhatsApp not configured', 'channel': 'whatsapp'}
            
            # Example WhatsApp integration (commented out)
            """
            url = f"https://graph.facebook.com/v15.0/{whatsapp_number}/messages"
            headers = {
                'Authorization': f'Bearer {api_token}',
                'Content-Type': 'application/json'
            }
            
            data = {
                'messaging_product': 'whatsapp',
                'to': order.customer_phone,
                'type': 'text',
                'text': {
                    'body': content['message']
                }
            }
            
            response = requests.post(url, json=data, headers=headers)
            """
            
            logger.info(f"WhatsApp notification would be sent to {order.customer_phone}")
            return {'success': True, 'channel': 'whatsapp', 'message': 'WhatsApp logged (integration needed)'}
            
        except Exception as e:
            logger.error(f"Failed to send WhatsApp notification: {e}")
            return {'success': False, 'error': str(e), 'channel': 'whatsapp'}
    
    def _send_push_notification(self, order, content, notification_type):
        """Send push notification (if user has web push enabled)"""
        
        try:
            # This would integrate with a push notification service
            # For now, we'll just log it
            
            logger.info(f"Push notification would be sent for order {order.order_id}")
            return {'success': True, 'channel': 'push', 'message': 'Push notification logged (integration needed)'}
            
        except Exception as e:
            logger.error(f"Failed to send push notification: {e}")
            return {'success': False, 'error': str(e), 'channel': 'push'}
    
    def send_admin_notification(self, subject, message, notification_type='info', order_id=None):
        """Send notification to admin"""
        
        try:
            # Send email to admin
            send_mail(
                subject=f'{self.site_name} Admin: {subject}',
                message=message,
                from_email=f'{self.site_name} <system@zetumart.co.ke>',
                recipient_list=[self.admin_email],
                fail_silently=False
            )
            
            # Create database notification for admin users
            admin_users = UserProfile.objects.filter(user__is_staff=True)
            
            for admin_profile in admin_users:
                Notification.objects.create(
                    user=admin_profile.user,
                    title=subject,
                    message=message,
                    notification_type=notification_type,
                    related_order_id=order_id,
                    is_read=False
                )
            
            logger.info(f"Admin notification sent: {subject}")
            return {'success': True}
            
        except Exception as e:
            logger.error(f"Failed to send admin notification: {e}")
            return {'success': False, 'error': str(e)}
    
    def send_promotional_notification(self, title, message, target_users=None):
        """Send promotional notifications to customers"""
        
        try:
            if target_users is None:
                # Send to all customers who have opted in
                target_users = UserProfile.objects.filter(
                    marketing_consent=True,
                    user__is_active=True
                )
            
            # Create database notifications
            notifications_created = 0
            for user_profile in target_users:
                Notification.objects.create(
                    user=user_profile.user,
                    title=title,
                    message=message,
                    notification_type='promotion',
                    is_read=False
                )
                notifications_created += 1
            
            # Send email campaign (optional)
            """
            email_list = [user.email for user in target_users if user.email]
            if email_list:
                send_mail(
                    subject=title,
                    message=message,
                    from_email=f'{self.site_name} <marketing@zetumart.co.ke>',
                    recipient_list=email_list,
                    fail_silently=True
                )
            """
            
            logger.info(f"Promotional notification sent to {notifications_created} users")
            return {'success': True, 'recipients': notifications_created}
            
        except Exception as e:
            logger.error(f"Failed to send promotional notification: {e}")
            return {'success': False, 'error': str(e)}
    
    def mark_notification_read(self, notification_id, user):
        """Mark a notification as read"""
        
        try:
            notification = Notification.objects.get(
                id=notification_id,
                user=user
            )
            notification.is_read = True
            notification.read_at = timezone.now()
            notification.save()
            
            return {'success': True}
            
        except Notification.DoesNotExist:
            return {'success': False, 'error': 'Notification not found'}
        except Exception as e:
            logger.error(f"Failed to mark notification as read: {e}")
            return {'success': False, 'error': str(e)}
    
    def get_user_notifications(self, user, unread_only=False, limit=20):
        """Get notifications for a user"""
        
        try:
            queryset = Notification.objects.filter(user=user).order_by('-created_at')
            
            if unread_only:
                queryset = queryset.filter(is_read=False)
            
            notifications = queryset[:limit]
            
            return {
                'success': True,
                'notifications': [
                    {
                        'id': n.id,
                        'title': n.title,
                        'message': n.message,
                        'type': n.notification_type,
                        'is_read': n.is_read,
                        'created_at': n.created_at.isoformat(),
                        'related_order_id': n.related_order_id
                    } for n in notifications
                ],
                'unread_count': Notification.objects.filter(user=user, is_read=False).count()
            }
            
        except Exception as e:
            logger.error(f"Failed to get user notifications: {e}")
            return {'success': False, 'error': str(e)}

# Utility function to trigger notifications
def trigger_order_notification(order, notification_type, additional_data=None):
    """Utility function to easily trigger order notifications"""
    
    notification_service = NotificationService()
    return notification_service.send_order_notification(order, notification_type, additional_data)
