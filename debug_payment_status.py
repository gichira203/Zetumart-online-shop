#!/usr/bin/env python3
"""
Debug Payment Status Detection Issues
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zetumart_project.settings')
django.setup()

from zetumart_app.models import Order, PaymentTransaction

def debug_payment_status():
    print("🔍 Debugging Payment Status Detection")
    print("=" * 60)
    
    # Check for recent orders and transactions
    print("\n📋 Recent Orders:")
    orders = Order.objects.all().order_by('-created_at')[:5]
    for order in orders:
        print(f"   Order {order.order_id}:")
        print(f"     Status: {order.order_status}")
        print(f"     Payment: {order.payment_status}")
        print(f"     Method: {order.payment_method}")
        
        # Get transactions for this order
        transactions = order.payment_transactions.all().order_by('-created_at')
        for trans in transactions:
            print(f"     Transaction {trans.id}:")
            print(f"       Status: {trans.status}")
            print(f"       Checkout ID: {trans.checkout_request_id}")
            print(f"       Result Code: {trans.result_code}")
            print(f"       Result Desc: {trans.result_desc}")
            print(f"       Created: {trans.created_at}")
        print()
    
    print("\n🔍 Issues Found:")
    
    # Issue 1: Check if transactions are being updated
    pending_transactions = PaymentTransaction.objects.filter(status='pending')
    print(f"   Pending transactions: {pending_transactions.count()}")
    
    # Issue 2: Check callback URL setup
    from django.conf import settings
    callback_url = getattr(settings, 'MPESA_CALLBACK_URL', '')
    print(f"   Callback URL: {callback_url}")
    if 'webhook.site' in callback_url:
        print("   ⚠️  Using webhook.site - callbacks won't reach your app!")
    
    # Issue 3: Check if status query is working
    print("\n🧪 Testing Status Query:")
    try:
        from zetumart_app.mpesa_service import MpesaService
        service = MpesaService()
        
        # Find a transaction with checkout ID
        test_trans = PaymentTransaction.objects.filter(
            checkout_request_id__isnull=False
        ).first()
        
        if test_trans:
            print(f"   Testing with transaction: {test_trans.checkout_request_id}")
            try:
                result = service.transaction_status_query(test_trans.checkout_request_id)
                print(f"   Query result: {result}")
            except Exception as e:
                print(f"   Query error: {e}")
        else:
            print("   No transactions with checkout request ID found")
            
    except Exception as e:
        print(f"   Service error: {e}")
    
    print("\n" + "=" * 60)
    print(" Root Causes of Payment Status Issues:")
    print("1. Callback URL not reachable (using webhook.site)")
    print("2. Transaction status not being updated from callbacks")
    print("3. Frontend polling logic not detecting status changes")
    print("4. Status query API not working or being called")
    
    print("\n💡 Solutions:")
    print("1. Set up proper callback URL (ngrok or production domain)")
    print("2. Ensure callbacks are updating transaction status")
    print("3. Fix frontend polling logic to check all status conditions")
    print("4. Add better error handling in status checking")

if __name__ == "__main__":
    debug_payment_status()
