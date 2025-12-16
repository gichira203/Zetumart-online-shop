from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    image1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)
    replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class Order(models.Model):
    ORDER_STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded')
    ]
    
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('partial_payment', 'Partial Payment'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded')
    ]
    
    DELIVERY_STATUS = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
        ('returned', 'Returned')
    ]
    
    PAYMENT_METHODS = [
        ('mpesa', 'M-Pesa STK Push'),
        ('till', 'M-Pesa Till/PayBill'),
        ('cod', 'Pay on Delivery'),
        ('polepole', 'Lipa Mdogo Mdogo'),
        ('card', 'Card Payment'),
        ('paypal', 'PayPal')
    ]
    
    order_id = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    
    # Order details
    items = models.JSONField()  # Store cart items as JSON
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Delivery information
    delivery_county = models.CharField(max_length=100)
    delivery_town = models.CharField(max_length=100)
    delivery_point = models.TextField()
    delivery_method = models.CharField(max_length=20, choices=[
        ('home', 'Home Delivery'),
        ('office', 'Office Delivery'),
        ('pickup', 'Pickup Station')
    ])
    delivery_time = models.CharField(max_length=20, choices=[
        ('anytime', 'Anytime'),
        ('morning', 'Morning (8AM-12PM)'),
        ('afternoon', 'Afternoon (12PM-5PM)'),
        ('evening', 'Evening (5PM-8PM)')
    ], default='anytime')
    delivery_instructions = models.TextField(blank=True, null=True)
    estimated_delivery_date = models.DateField(null=True, blank=True)
    
    # Payment information
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    payment_details = models.JSONField(null=True, blank=True)  # Store payment-specific details
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    
    # Status tracking
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS, default='pending')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.order_id} - {self.customer_name}"
    
    def save(self, *args, **kwargs):
        if not self.order_id:
            # Generate unique order ID
            import datetime
            today = datetime.date.today()
            last_order = Order.objects.filter(created_at__date=today).order_by('-id').first()
            if last_order:
                last_number = int(last_order.order_id[2:])  # Remove 'ZM' prefix
                new_number = last_number + 1
            else:
                new_number = 1
            self.order_id = f"ZM{new_number:04d}"
        super().save(*args, **kwargs)

class ChatMessage(models.Model):
    MESSAGE_TYPES = [
        ('general', 'General Inquiry'),
        ('order', 'Order Related'),
        ('payment', 'Payment Issue'),
        ('delivery', 'Delivery Issue'),
        ('product', 'Product Question'),
        ('return', 'Return/Refund'),
        ('complaint', 'Complaint')
    ]
    
    SENDER_TYPES = [
        ('customer', 'Customer'),
        ('admin', 'Admin')
    ]
    
    session_id = models.CharField(max_length=100)  # For grouping conversations
    sender_type = models.CharField(max_length=20, choices=SENDER_TYPES)
    
    # Customer information (for customer messages)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.EmailField(blank=True, null=True)
    customer_phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Message details
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES, default='general')
    message = models.TextField()
    
    # Admin information (for admin replies)
    admin_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Status
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        sender = self.customer_name or (self.admin_user.username if self.admin_user else 'Unknown')
        return f"{self.sender_type.title()}: {sender} - {self.message[:50]}..."
    
    class Meta:
        ordering = ['created_at']

class OrderTracking(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='tracking_updates')
    status = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.order.order_id} - {self.status}"
    
    class Meta:
        ordering = ['-timestamp']

class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[
        ('admin', 'Admin'),
        ('superadmin', 'Super Admin')
    ], default='admin')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class CustomerCareMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True, help_text="WhatsApp number with country code")
    subject = models.CharField(max_length=200, blank=True, null=True)
    message_type = models.CharField(max_length=20, choices=[
        ('ai', 'AI Chat'),
        ('agent', 'Agent Chat')
    ], default='agent')
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        if self.user:
            return f"Message from {self.user.username}"
        return f"Message from {self.name or 'Anonymous'}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Notification for {self.user.username}"
