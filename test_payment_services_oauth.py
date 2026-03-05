#!/usr/bin/env python3
"""
Test the specific OAuth method used in payment_services.py
"""

import requests

def test_payment_services_oauth():
    print("🔍 Testing payment_services.py OAuth Method")
    print("=" * 60)
    
    # Use the same credentials as payment_services.py
    consumer_key = 'lAPb8KTpWSqcgr1PWDyzbeyRRhuq8AqZzoh2CqrWuXEp71qy'
    consumer_secret = '6tyMucRrUdEYbSm5cwX4S9kMZDAA3e78ADdMjeCprELZoZkJ6WZAVDaFLVVGyZLc'
    
    print(f"🔑 Consumer Key: {consumer_key[:20]}...")
    print(f"🔑 Consumer Secret: {consumer_secret[:20]}...")
    
    try:
        # Test the exact method from payment_services.py
        api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        print(f"\n📡 Testing URL: {api_url}")
        
        # This is the method used in payment_services.py
        response = requests.get(
            api_url,
            auth=(consumer_key, consumer_secret)
        )
        
        print(f"📊 Status: {response.status_code}")
        print(f"📄 Response: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            token = data.get('access_token')
            print(f"✅ SUCCESS: Token obtained: {token[:30]}...")
        else:
            print(f"❌ FAILED: {response.status_code}")
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("💡 If this method fails but manual Basic Auth works:")
    print("1. The auth=(user,pass) method might have issues")
    print("2. Manual Basic Auth headers are more reliable")
    print("3. Consider using the mpesa_service.py implementation")

if __name__ == "__main__":
    test_payment_services_oauth()
