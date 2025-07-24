#!/usr/bin/env python
"""
Manual test to check login redirects by accessing views directly.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexas_project.settings')
django.setup()

from django.test import RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.backends.db import SessionStore

from apps.donation_dashboard.views import donor_dashboard
from apps.campaign_dashboard.views import campaign_manager_dashboard

User = get_user_model()

def test_views_directly():
    """Test the dashboard views directly."""
    
    print("Testing Dashboard Views Directly")
    print("=" * 35)
    
    factory = RequestFactory()
    
    # Test donation dashboard
    print("\n1. Testing Donation Dashboard View...")
    try:
        donor_user = User.objects.get(email='donor@nexas.org')
        print(f"Found donor user: {donor_user.email}, role: {donor_user.role}")
        
        # Create request
        request = factory.get('/dashboard/donation/')
        request.user = donor_user
        
        # Add session and messages (required for Django views)
        request.session = SessionStore()
        request._messages = FallbackStorage(request)
        
        # Call the view
        response = donor_dashboard(request)
        print(f"Donation dashboard status: {response.status_code}")
        
        if hasattr(response, 'content'):
            content_preview = response.content[:200] if response.content else "No content"
            print(f"Content preview: {content_preview}")
        
    except User.DoesNotExist:
        print("Donor user not found")
    except Exception as e:
        print(f"Error testing donation dashboard: {e}")
        import traceback
        traceback.print_exc()
    
    # Test campaign dashboard
    print("\n2. Testing Campaign Dashboard View...")
    try:
        campaign_user = User.objects.get(email='campaign@nexas.org')
        print(f"Found campaign user: {campaign_user.email}, role: {campaign_user.role}")
        
        # Create request
        request = factory.get('/dashboard/campaign/')
        request.user = campaign_user
        
        # Add session and messages
        request.session = SessionStore()
        request._messages = FallbackStorage(request)
        
        # Call the view
        response = campaign_manager_dashboard(request)
        print(f"Campaign dashboard status: {response.status_code}")
        
        if hasattr(response, 'content'):
            content_preview = response.content[:200] if response.content else "No content"
            print(f"Content preview: {content_preview}")
        
    except User.DoesNotExist:
        print("Campaign user not found")
    except Exception as e:
        print(f"Error testing campaign dashboard: {e}")
        import traceback
        traceback.print_exc()

def check_users():
    """Check if our test users exist and have correct passwords."""
    print("\nChecking Test Users")
    print("=" * 18)
    
    test_users = ['donor@nexas.org', 'campaign@nexas.org']
    
    for email in test_users:
        try:
            user = User.objects.get(email=email)
            print(f"User: {email}")
            print(f"  Role: {user.role}")
            print(f"  Active: {user.is_active}")
            print(f"  Has password: {bool(user.password)}")
            print(f"  Password check: {user.check_password('nexas123')}")
            print(f"  Dashboard URL: {user.get_dashboard_url()}")
            print()
        except User.DoesNotExist:
            print(f"User {email} not found")

if __name__ == '__main__':
    check_users()
    test_views_directly()
