from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.admin_dashboard_view, name='admin'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('contact/', views.contact_view, name='contact'),
    path('profile/', views.profile_view, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('customer-care/', views.customer_care_view, name='customer_care'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('reply-message/<int:message_id>/', views.reply_to_message, name='reply_to_message'),
    path('delete-message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('api/admin/users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('api/admin/users/add/', views.add_admin_user, name='add_admin_user'),
    path('export-users-excel/', views.export_users_excel, name='export_users_excel'),
    path('export-users-word/', views.export_users_word, name='export_users_word'),
    path('export-users-pdf/', views.export_users_pdf, name='export_users_pdf'),
    path('api/admin/products/', views.add_product, name='add_product'),
    path('api/admin/products/list/', views.get_products, name='get_products'),
    path('api/admin/products/<int:product_id>/', views.get_product, name='get_product'),
    path('api/admin/products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('api/admin/products/<int:product_id>/delete/', views.delete_product_view, name='delete_product'),
    path('delete-product/<int:product_id>/', views.delete_product_view, name='delete_product_simple'),
    path('products/', views.products_view, name='products'),
    path('shop/', views.shop_category_view, name='shop_category'),
    path('api/categories/', views.get_categories, name='get_categories'),
    path('api/products/', views.get_products, name='get_products_api'),
    path('api/products/<int:product_id>/', views.get_product, name='get_product_api'),
    path('api/products/<int:product_id>/update/', views.update_product, name='update_product_api'),
    path('api/products/<int:product_id>/delete/', views.delete_product_view, name='delete_product_api'),
    path('api/products/add/', views.add_product, name='add_product_api'),
    
    # Order Management API
    path('api/orders/create/', views.create_order, name='create_order'),
    path('api/orders/', views.get_orders, name='get_orders'),
    path('api/orders/<int:order_id>/update/', views.update_order_status, name='update_order_status'),
    path('api/orders/<int:order_id>/tracking/', views.get_order_tracking, name='get_order_tracking'),
    
    # Chat System API
    path('api/chat/send/', views.send_chat_message, name='send_chat_message'),
    path('api/chat/messages/', views.get_chat_messages, name='get_chat_messages'),
    path('api/chat/reply/<int:message_id>/', views.reply_to_chat_message, name='reply_to_chat_message'),
    
    # Checkout and Payment
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-confirmation/<str:order_id>/', views.order_confirmation_view, name='order_confirmation'),
    path('api/orders/<str:order_id>/details/', views.get_order_details, name='get_order_details'),
    path('api/orders/<str:order_id>/payment-status/', views.get_payment_status, name='get_payment_status'),
    path('payment/success/', views.payment_success_view, name='payment_success'),
    path('payment/cancel/', views.payment_cancel_view, name='payment_cancel'),
    path('api/mpesa/callback/', views.mpesa_callback, name='mpesa_callback'),
    
    # Delivery API endpoints
    path('api/delivery/search-counties/', views.api_search_counties, name='api_search_counties'),
    path('api/delivery/get-cities/', views.api_get_cities, name='api_get_cities'),
    path('api/delivery/get-info/', views.api_get_delivery_info, name='api_get_delivery_info'),
    path('api/delivery/calculate-fee/', views.api_calculate_delivery_fee, name='api_calculate_delivery_fee'),
    
    # Superuser Admin Management
    path('api/admin/users/', views.admin_user_management, name='admin_user_management'),
    path('api/admin/products/manage/', views.admin_product_management, name='admin_product_management'),
    path('api/admin/messages/manage/', views.admin_message_management, name='admin_message_management'),
]