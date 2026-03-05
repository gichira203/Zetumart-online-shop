#!/usr/bin/env python3
"""
Test M-Pesa credentials in Django context
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

from django.conf import settings

def test_django_credentials():
    print("🔍 Testing M-Pesa Credentials in Django Context")
    print("=" * 60)
    
    # Check what Django is loading
    print(f"🔑 Consumer Key: {getattr(settings, 'MPESA_CONSUMER_KEY', 'NOT SET')}")
    print(f"🔑 Consumer Secret: {getattr(settings, 'MPESA_CONSUMER_SECRET', 'NOT SET')}")
    print(f"🔑 Passkey: {getattr(settings, 'MPESA_PASSKEY', 'NOT SET')}")
    print(f"🔑 Business Shortcode: {getattr(settings, 'MPESA_BUSINESS_SHORTCODE', 'NOT SET')}")
    print(f"🔗 Callback URL: {getattr(settings, 'MPESA_CALLBACK_URL', 'NOT SET')}")
    print(f"🌐 Base URL: {'https://sandbox.safaricom.co.ke' if settings.DEBUG else 'https://api.safaricom.co.ke'}")
    
    # Test the actual service
    print("\n🧪 Testing MpesaService...")
    try:
        from zetumart_app.mpesa_service import MpesaService
        service = MpesaService()
        
        print(f"   Service Consumer Key: {service.consumer_key[:20]}...")
        print(f"   Service Consumer Secret: {service.consumer_secret[:20]}...")
        print(f"   Service Base URL: {service.base_url}")
        
        # Test token generation
        print("\n🚀 Testing token generation...")
        token = service.get_access_token()
        if token:
            print(f"   ✅ SUCCESS: Token obtained: {token[:30]}...")
        else:
            print("   ❌ FAILED: No token returned")
            
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("💡 If this test fails but the standalone test works:")
    print("1. Check Django settings are loading correctly")
    print("2. Verify no environment variables are overriding settings")
    print("3. Check for whitespace in credentials")
    print("4. Ensure Django can make outbound requests")

if __name__ == "__main__":
    test_django_credentials()
