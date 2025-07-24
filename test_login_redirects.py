#!/usr/bin/env python
"""
Test login redirections for different user roles.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexas_project.settings')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

def test_login_redirections():
    """Test that users are redirected to correct dashboards after login."""
    
    print("Testing Login Redirections")
    print("=" * 30)
    
    # Create a test client
    client = Client()
    
    # Test users to check
    test_users = [
        {
            'email': 'donor@nexas.org',
            'role': 'donation',
            'expected_redirect': '/dashboard/donation/'
        },
        {
            'email': 'campaign@nexas.org', 
            'role': 'campaign',
            'expected_redirect': '/dashboard/campaign/'
        }
    ]
    
    for user_data in test_users:
        print(f"\n--- Testing {user_data['role']} user ---")
        
        # Check if user exists
        try:
            user = User.objects.get(email=user_data['email'])
            print(f"User found: {user.email} (role: {user.role})")
            
            # Test the get_dashboard_url method
            expected_url = user.get_dashboard_url()
            print(f"Expected dashboard URL: {expected_url}")
            
            # Test login
            login_data = {
                'username': user_data['email'],
                'password': 'nexas123'
            }
            
            print(f"Attempting login with {user_data['email']}...")
            response = client.post('/accounts/login/', login_data, follow=True)
            
            print(f"Response status: {response.status_code}")
            print(f"Final URL: {response.wsgi_request.path}")
            
            # Check if redirected to correct dashboard
            if response.wsgi_request.path == user_data['expected_redirect']:
                print(f"✅ PASS: Correctly redirected to {user_data['expected_redirect']}")
            else:
                print(f"❌ FAIL: Expected {user_data['expected_redirect']}, got {response.wsgi_request.path}")
            
            # Test direct access to dashboard
            print(f"Testing direct access to {user_data['expected_redirect']}...")
            dashboard_response = client.get(user_data['expected_redirect'])
            print(f"Dashboard access status: {dashboard_response.status_code}")
            
            if dashboard_response.status_code == 200:
                print("✅ PASS: Dashboard accessible")
                # Check if it's using the correct template
                if hasattr(dashboard_response, 'templates'):
                    templates = [t.name for t in dashboard_response.templates]
                    print(f"Templates used: {templates}")
                else:
                    print("Template info not available")
            else:
                print(f"❌ FAIL: Dashboard returned status {dashboard_response.status_code}")
                if hasattr(dashboard_response, 'content'):
                    print("Response content preview:", dashboard_response.content[:200])
            
            # Logout for next test
            client.logout()
            
        except User.DoesNotExist:
            print(f"❌ User {user_data['email']} not found")
        except Exception as e:
            print(f"❌ Error testing {user_data['email']}: {e}")
    
    print(f"\nLogin redirection test completed!")

def check_url_patterns():
    """Check if URL patterns are correctly configured."""
    print("\nChecking URL Patterns")
    print("=" * 20)
    
    try:
        # Test URL resolution
        donation_url = reverse('donation_dashboard:donor_dashboard')
        print(f"Donation dashboard URL: {donation_url}")
        
        campaign_url = reverse('campaign_dashboard:dashboard') 
        print(f"Campaign dashboard URL: {campaign_url}")
        
        print("✅ URL patterns resolved correctly")
        
    except Exception as e:
        print(f"❌ URL pattern error: {e}")

if __name__ == '__main__':
    check_url_patterns()
    test_login_redirections()
