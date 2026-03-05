#!/usr/bin/env python3
"""
Comprehensive M-Pesa Diagnostic Tool
This helps identify when and why the 400 OAuth error occurs
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

def comprehensive_diagnostic():
    print("🔍 COMPREHENSIVE M-PESA DIAGNOSTIC")
    print("=" * 60)
    
    # Test 1: Check both services
    print("\n📱 Test 1: Both M-Pesa Services")
    try:
        from zetumart_app.mpesa_service import MpesaService
        from zetumart_app.payment_services import MpesaPaymentService
        
        print("   Testing MpesaService...")
        service1 = MpesaService()
        token1 = service1.get_access_token()
        print(f"   ✅ MpesaService Token: {token1[:20] if token1 else 'None'}...")
        
        print("   Testing MpesaPaymentService...")
        service2 = MpesaPaymentService()
        token2 = service2.get_access_token()
        print(f"   ✅ MpesaPaymentService Token: {token2[:20] if token2 else 'None'}...")
        
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
    
    # Test 2: Check network connectivity
    print("\n🌐 Test 2: Network Connectivity")
    try:
        import requests
        response = requests.get("https://sandbox.safaricom.co.ke", timeout=10)
        print(f"   ✅ Sandbox reachable: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Network error: {e}")
    
    # Test 3: Check for potential credential corruption
    print("\n🔍 Test 3: Credential Integrity Check")
    from django.conf import settings
    
    credentials = {
        'MPESA_CONSUMER_KEY': getattr(settings, 'MPESA_CONSUMER_KEY', ''),
        'MPESA_CONSUMER_SECRET': getattr(settings, 'MPESA_CONSUMER_SECRET', ''),
        'MPESA_PASSKEY': getattr(settings, 'MPESA_PASSKEY', ''),
        'MPESA_BUSINESS_SHORTCODE': getattr(settings, 'MPESA_BUSINESS_SHORTCODE', ''),
    }
    
    for key, value in credentials.items():
        issues = []
        if not value:
            issues.append("EMPTY")
        elif len(value) < 10:
            issues.append("TOO_SHORT")
        elif '\n' in value or '\r' in value:
            issues.append("CONTAINS_NEWLINE")
        elif value.strip() != value:
            issues.append("HAS_WHITESPACE")
        
        status = "✅ OK" if not issues else f"❌ {', '.join(issues)}"
        print(f"   {key}: {status}")
    
    # Test 4: Simulate high-frequency requests
    print("\n⚡ Test 4: High-Frequency Requests")
    try:
        from zetumart_app.mpesa_service import MpesaService
        
        for i in range(5):
            service = MpesaService()
            token = service.get_access_token()
            print(f"   Request {i+1}: {'✅' if token else '❌'}")
            
    except Exception as e:
        print(f"   ❌ High-frequency error: {e}")
    
    # Test 5: Check Django logging configuration
    print("\n📝 Test 5: Django Logging")
    import logging
    
    loggers = ['zetumart_app.mpesa_service', 'zetumart_app.payment_services']
    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        print(f"   {logger_name}: Level={logger.level}, Handlers={len(logger.handlers)}")
    
    print("\n" + "=" * 60)
    print("🎯 NEXT STEPS:")
    print("1. Run your actual application and watch for the 400 error")
    print("2. Check Django logs for the detailed debug output we added")
    print("3. Note exactly when the error occurs (which view/action)")
    print("4. The error might be environment-specific or timing-related")
    print("5. If the error persists, check for any middleware affecting requests")

if __name__ == "__main__":
    comprehensive_diagnostic()
