from django.contrib import admin
from .models import Category, Product, ContactMessage, Order, ChatMessage, OrderTracking, AdminUser, UserProfile, CustomerCareMessage, Notification

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']
    ordering = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock', 'status', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']
    readonly_fields = ['created_at']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'replied', 'created_at']
    list_filter = ['replied', 'created_at']
    search_fields = ['name', 'email', 'subject']
    ordering = ['-created_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer_name', 'total_amount', 'order_status', 'payment_status', 'created_at']
    list_filter = ['order_status', 'payment_status', 'delivery_status', 'payment_method', 'created_at']
    search_fields = ['order_id', 'customer_name', 'customer_email']
    ordering = ['-created_at']
    readonly_fields = ['order_id', 'created_at', 'updated_at']

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'sender_type', 'message_type', 'is_read', 'created_at']
    list_filter = ['sender_type', 'message_type', 'is_read', 'created_at']
    search_fields = ['session_id', 'customer_name', 'message']
    ordering = ['-created_at']

@admin.register(OrderTracking)
class OrderTrackingAdmin(admin.ModelAdmin):
    list_display = ['order', 'status', 'location', 'timestamp']
    list_filter = ['status', 'timestamp']
    search_fields = ['order__order_id', 'status', 'location']
    ordering = ['-timestamp']

@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'created_at']
    list_filter = ['role', 'created_at']
    search_fields = ['user__username', 'user__email']
    ordering = ['-created_at']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'date_of_birth', 'created_at']
    search_fields = ['user__username', 'user__email', 'phone']
    ordering = ['-created_at']

@admin.register(CustomerCareMessage)
class CustomerCareMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message_type', 'is_read', 'is_replied', 'created_at']
    list_filter = ['message_type', 'is_read', 'is_replied', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    ordering = ['-created_at']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['user__username', 'message']
    ordering = ['-created_at']
