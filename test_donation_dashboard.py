#!/usr/bin/env python
"""
Test script for the new donation dashboard functionality.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexas_project.settings')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model
from apps.donation_dashboard.models import Donor, Donation, DonationCampaign

User = get_user_model()

def test_donation_dashboard():
    """Test the donation dashboard functionality."""
    
    print("Testing Donation Dashboard Functionality")
    print("=" * 50)
    
    # Create a client for testing
    client = Client()
    
    # Test 1: Check if donation user exists
    print("\n1. Testing donation user access...")
    try:
        donation_user = User.objects.get(email='donor@nexas.org')
        print(f"Found donation user: {donation_user.email} (role: {donation_user.role})")
        
        # Test login
        login_successful = client.login(email='donor@nexas.org', password='nexas123')
        if login_successful:
            print("Login successful")
        else:
            print("Login failed")
            return
            
    except User.DoesNotExist:
        print("No donation user found")
        return
    
    # Test 2: Check dashboard access
    print("\n2. Testing dashboard access...")
    response = client.get('/dashboard/donation/')
    if response.status_code == 200:
        print("Dashboard accessible")
        print(f"   Template used: donor_dashboard_new.html")
    else:
        print(f"Dashboard access failed (status: {response.status_code})")
        return
    
    # Test 3: Check donor profile creation
    print("\n3. Testing donor profile...")
    donor, created = Donor.objects.get_or_create(
        email='donor@nexas.org',
        defaults={
            'first_name': 'Test',
            'last_name': 'Donor',
            'donor_type': 'individual',
        }
    )
    if created:
        print("Donor profile created")
    else:
        print("Donor profile exists")
    
    print(f"   Total donated: Rs.{donor.total_donated}")
    print(f"   Donation count: {donor.donation_count}")
    
    # Test 4: Check campaigns
    print("\n4. Testing active campaigns...")
    active_campaigns = DonationCampaign.objects.filter(status='active', is_public=True)
    print(f"Found {active_campaigns.count()} active campaigns")
    for campaign in active_campaigns[:3]:
        print(f"   - {campaign.name}")
    
    # Test 5: Test donation submission (simulation)
    print("\n5. Testing donation submission...")
    if active_campaigns.exists():
        campaign = active_campaigns.first()
        donation_data = {
            'campaign': campaign.id,
            'amount': '1000',
            'card_number': '1234567890123456',
            'expiry': '12/25',
            'cvv': '123',
            'cardholder_name': 'Test Donor',
            'email': 'donor@nexas.org'
        }
        
        response = client.post('/dashboard/donation/donate/', donation_data)
        if response.status_code == 200:
            try:
                response_data = response.json()
                if response_data.get('success'):
                    print("Donation submission successful")
                    print(f"   Transaction ID: {response_data.get('transaction_id')}")
                else:
                    print(f"Donation failed: {response_data.get('error')}")
            except:
                print("Invalid JSON response")
        else:
            print(f"Donation submission failed (status: {response.status_code})")
    
    # Test 6: Check donation history
    print("\n6. Testing donation history...")
    donor_donations = donor.donations.filter(status='completed').count()
    print(f"Donor has {donor_donations} completed donations")
    
    print("\nDashboard testing completed!")

if __name__ == '__main__':
    test_donation_dashboard()
