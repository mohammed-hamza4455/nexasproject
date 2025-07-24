#!/usr/bin/env python
"""
Simple test for login redirections.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexas_project.settings')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model

User = get_user_model()

def test_redirections():
    """Test login redirections."""
    
    print("Testing Login Redirections")
    print("=" * 30)
    
    client = Client()
    
    # Test donation user
    print("\n1. Testing donation user...")
    try:
        user = User.objects.get(email='donor@nexas.org')
        print(f"Found user: {user.email}, role: {user.role}")
        print(f"Expected dashboard URL: {user.get_dashboard_url()}")
        
        # Try login
        response = client.post('/accounts/login/', {
            'username': 'donor@nexas.org',
            'password': 'nexas123'
        }, follow=True)
        
        print(f"Login response status: {response.status_code}")
        print(f"Final URL after login: {response.wsgi_request.path}")
        
        # Try direct access
        dashboard_response = client.get('/dashboard/donation/')
        print(f"Direct dashboard access status: {dashboard_response.status_code}")
        
        client.logout()
        
    except User.DoesNotExist:
        print("Donation user not found")
    except Exception as e:
        print(f"Error with donation user: {e}")
    
    # Test campaign user  
    print("\n2. Testing campaign user...")
    try:
        user = User.objects.get(email='campaign@nexas.org')
        print(f"Found user: {user.email}, role: {user.role}")
        print(f"Expected dashboard URL: {user.get_dashboard_url()}")
        
        # Try login
        response = client.post('/accounts/login/', {
            'username': 'campaign@nexas.org',
            'password': 'nexas123'
        }, follow=True)
        
        print(f"Login response status: {response.status_code}")
        print(f"Final URL after login: {response.wsgi_request.path}")
        
        # Try direct access
        dashboard_response = client.get('/dashboard/campaign/')
        print(f"Direct dashboard access status: {dashboard_response.status_code}")
        
    except User.DoesNotExist:
        print("Campaign user not found")
    except Exception as e:
        print(f"Error with campaign user: {e}")

if __name__ == '__main__':
    test_redirections()
