#!/usr/bin/env python3
"""
Test the fixed payment status detection
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

from django.test import RequestFactory
from zetumart_app.views import check_payment_status

def test_payment_status_fix():
    print("🧪 Testing Payment Status Detection Fix")
    print("=" * 60)
    
    # Create a mock request
    factory = RequestFactory()
    
    # Find an order with pending transaction
    from zetumart_app.models import Order, PaymentTransaction
    
    pending_order = Order.objects.filter(
        payment_transactions__status='pending',
        payment_transactions__checkout_request_id__isnull=False
    ).first()
    
    if not pending_order:
        print("❌ No pending transactions found to test")
        return
    
    print(f"📋 Testing with Order: {pending_order.order_id}")
    
    # Get the pending transaction
    pending_trans = pending_order.payment_transactions.filter(
        status='pending'
    ).first()
    
    print(f"🔍 Transaction: {pending_trans.checkout_request_id}")
    print(f"   Current Status: {pending_trans.status}")
    print(f"   Current Order Status: {pending_order.order_status}")
    
    # Test the check_payment_status endpoint
    request = factory.get(f'/api/mpesa/check-payment/?order_id={pending_order.order_id}')
    
    try:
        response = check_payment_status(request)
        result = response.getvalue()
        
        print(f"\n📊 Response Status: {response.status_code}")
        
        # Parse JSON response
        import json
        response_data = json.loads(result.decode('utf-8'))
        
        print(f"📋 Response Data:")
        for key, value in response_data.items():
            print(f"   {key}: {value}")
        
        # Check if status was updated
        pending_trans.refresh_from_db()
        pending_order.refresh_from_db()
        
        print(f"\n🔄 Updated Status:")
        print(f"   Transaction Status: {pending_trans.status}")
        print(f"   Order Status: {pending_order.order_status}")
        print(f"   Payment Status: {pending_order.payment_status}")
        print(f"   Result Code: {pending_trans.result_code}")
        print(f"   Result Desc: {pending_trans.result_desc}")
        
        # Verify the fix worked
        if pending_trans.status in ['completed', 'cancelled', 'failed']:
            print(f"\n✅ SUCCESS: Transaction status was updated!")
        else:
            print(f"\n⚠️  Transaction still pending - may need manual check")
            
    except Exception as e:
        print(f"❌ Error testing endpoint: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("💡 Next Steps:")
    print("1. Test with a real M-Pesa payment")
    print("2. Verify frontend detects status changes")
    print("3. Check that loading state is cleared properly")

if __name__ == "__main__":
    test_payment_status_fix()
