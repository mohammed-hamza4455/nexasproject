#!/usr/bin/env python
"""
Test server access with requests library.
"""

import requests
import sys

def test_server_running():
    """Test if the development server is accessible."""
    
    print("Testing Server Access")
    print("=" * 20)
    
    base_url = "http://127.0.0.1:8000"
    
    try:
        # Test if server is running
        print("1. Testing server connection...")
        response = requests.get(base_url, timeout=5)
        print(f"Server response: {response.status_code}")
        
        # Test login page
        print("\n2. Testing login page...")
        login_response = requests.get(f"{base_url}/accounts/login/", timeout=5)
        print(f"Login page status: {login_response.status_code}")
        
        # Test dashboard URLs directly (should redirect to login)
        print("\n3. Testing dashboard URLs (without auth)...")
        
        dashboards = [
            "/dashboard/donation/",
            "/dashboard/campaign/"
        ]
        
        for dashboard in dashboards:
            resp = requests.get(f"{base_url}{dashboard}", allow_redirects=False, timeout=5)
            print(f"{dashboard}: {resp.status_code}")
            if resp.status_code in [301, 302]:
                print(f"  Redirects to: {resp.headers.get('Location', 'Unknown')}")
        
        print("\nServer tests completed successfully!")
        return True
        
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to server. Make sure 'python manage.py runserver' is running.")
        return False
    except requests.exceptions.Timeout:
        print("ERROR: Server request timed out.")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == '__main__':
    success = test_server_running()
    if not success:
        print("\nPlease start the development server with:")
        print("python manage.py runserver")
        sys.exit(1)
