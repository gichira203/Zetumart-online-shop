from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('contact/', views.contact_view, name='contact'),
    path('profile/', views.profile_view, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('customer-care/', views.customer_care_view, name='customer_care'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('reply-message/<int:message_id>/', views.reply_to_message, name='reply_to_message'),
    path('export-users-excel/', views.export_users_excel, name='export_users_excel'),
    path('export-users-word/', views.export_users_word, name='export_users_word'),
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
    
    # Payment
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('api/orders/<str:order_id>/details/', views.get_order_details, name='get_order_details'),
    path('api/orders/<str:order_id>/payment-status/', views.get_payment_status, name='get_payment_status'),
    path('api/mpesa/initiate-stk/', views.initiate_stk_push, name='initiate_stk_push'),
    path('api/mpesa/callback/', views.mpesa_callback, name='mpesa_callback'),
    path('api/mpesa/check-payment/', views.check_payment_status, name='check_payment_status'),
    path('api/mpesa/verify-transaction/', views.verify_transaction_code, name='verify_transaction_code'),
    
    # Delivery API endpoints
    path('api/delivery/search-counties/', views.api_search_counties, name='api_search_counties'),
    path('api/delivery/get-cities/', views.api_get_cities, name='api_get_cities'),
    path('api/delivery/get-info/', views.api_get_delivery_info, name='api_get_delivery_info'),
    path('api/delivery/calculate-fee/', views.api_calculate_delivery_fee, name='api_calculate_delivery_fee'),
    
    # Product Details API for checkout
    path('api/products/details/', views.api_products_details, name='api_products_details'),
    
    # ============ ADMIN DASHBOARD ============
    # Dashboard
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Redirect old admin product URLs to main products page
    path('admin/products/', views.redirect_to_products, name='admin_products_redirect'),
    
    # Product Management URLs (removed - using main products page instead)
    
    # Other Admin Management URLs
    path('admin/users/', views.admin_user_management, name='admin_user_management'),
    path('admin/orders/', views.admin_order_management, name='admin_order_management'),
    path('admin/elements/', views.admin_elements, name='admin_elements'),
    path('admin/reports/', views.admin_reports, name='admin_reports'),
    path('admin/calendar/', views.admin_calendar, name='admin_calendar'),
    path('admin/files/', views.admin_files, name='admin_files'),
    path('admin/messages/', views.admin_message_management, name='admin_message_management'),
    path('admin/messages/reply/<int:message_id>/', views.admin_reply_message, name='admin_reply_message'),
    path('admin/messages/mark-replied/<int:message_id>/', views.admin_mark_message_replied, name='admin_mark_message_replied'),
    path('admin/settings/', views.admin_settings, name='admin_settings'),
    path('test-edit/', views.test_edit_button, name='test_edit_button'),
    path('real-test/', views.real_browser_test, name='real_browser_test'),
]