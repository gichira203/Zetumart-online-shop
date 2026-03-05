#!/usr/bin/env python3
"""
Test M-Pesa service in actual usage scenarios
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

from zetumart_app.mpesa_service import MpesaService

def test_actual_usage():
    print("🧪 Testing M-Pesa Service in Actual Usage Scenarios")
    print("=" * 60)
    
    # Test 1: Fresh service instance (like in views)
    print("\n📱 Test 1: Fresh Service Instance")
    try:
        mpesa_service = MpesaService()
        print("   ✅ Service created successfully")
        
        # Test token generation
        token = mpesa_service.get_access_token()
        print(f"   ✅ Token: {token[:30] if token else 'None'}...")
        
        # Test STK push with minimal data
        result = mpesa_service.stk_push_request(
            phone_number="254712345678",
            amount=10,
            order_id="TEST001"
        )
        print(f"   📊 STK Result: {result}")
        
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
    
    # Test 2: Multiple service instances (like concurrent requests)
    print("\n🔄 Test 2: Multiple Service Instances")
    try:
        for i in range(3):
            print(f"   📱 Instance {i+1}:")
            mpesa_service = MpesaService()
            token = mpesa_service.get_access_token()
            print(f"      Token: {token[:20] if token else 'None'}...")
            
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
    
    # Test 3: Check for environment variable overrides
    print("\n🌍 Test 3: Environment Variables Check")
    env_vars = [
        'MPESA_CONSUMER_KEY',
        'MPESA_CONSUMER_SECRET', 
        'MPESA_PASSKEY',
        'MPESA_BUSINESS_SHORTCODE',
        'MPESA_CALLBACK_URL'
    ]
    
    for var in env_vars:
        value = os.environ.get(var, 'NOT SET')
        print(f"   {var}: {value[:30] if value != 'NOT SET' else value}")
    
    # Test 4: Check Django settings vs environment
    print("\n⚙️ Test 4: Django Settings vs Environment")
    from django.conf import settings
    
    for var in env_vars:
        django_value = getattr(settings, var, 'NOT SET')
        env_value = os.environ.get(var, 'NOT SET')
        match = "✅" if str(django_value) == str(env_value) else "❌"
        print(f"   {var}: Django={str(django_value)[:30]} Env={str(env_value)[:30]} {match}")
    
    print("\n" + "=" * 60)
    print("💡 If you're still getting 400 errors:")
    print("1. Check your Django logs for the detailed debug output")
    print("2. Look for any environment variable overrides")
    print("3. Check if the error happens in specific views only")
    print("4. Verify the exact request that's failing")

if __name__ == "__main__":
    test_actual_usage()
