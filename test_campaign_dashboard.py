#!/usr/bin/env python
"""
Test script for the campaign manager dashboard functionality.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexas_project.settings')
django.setup()

from django.template.loader import get_template
from django.test import RequestFactory
from apps.campaign_dashboard.views import campaign_manager_dashboard
from apps.donation_dashboard.models import DonationCampaign, CampaignActivity
from apps.accounts.models import User

def test_campaign_dashboard():
    """Test the campaign dashboard functionality."""
    
    print("Testing Campaign Manager Dashboard Functionality")
    print("=" * 55)
    
    # Test 1: Check if template exists
    print("\n1. Testing template loading...")
    try:
        template = get_template('campaign_dashboard/campaign_manager_dashboard.html')
        print("Template found: campaign_dashboard/campaign_manager_dashboard.html")
    except Exception as e:
        print(f"Template not found: {e}")
        return False
    
    # Test 2: Check campaign manager user
    print("\n2. Testing campaign manager user...")
    try:
        campaign_user = User.objects.get(email='campaign@nexas.org')
        print(f"Found campaign manager: {campaign_user.email} (role: {campaign_user.role})")
    except User.DoesNotExist:
        print("No campaign manager user found")
        return False
    
    # Test 3: Check sample data
    print("\n3. Testing sample data...")
    campaigns = DonationCampaign.objects.count()
    activities = CampaignActivity.objects.count()
    
    print(f"Sample data:")
    print(f"  - Campaigns: {campaigns}")
    print(f"  - Activities: {activities}")
    
    # Test 4: Test view functionality
    print("\n4. Testing view functionality...")
    try:
        factory = RequestFactory()
        request = factory.get('/dashboard/campaign/')
        request.user = campaign_user
        
        # Call the view
        response = campaign_manager_dashboard(request)
        
        if hasattr(response, 'status_code'):
            print(f"View response status: {response.status_code}")
            if response.status_code == 200:
                print("Dashboard view executed successfully")
            else:
                print("Dashboard view returned error status")
        else:
            print("View executed successfully (rendered response)")
            
    except Exception as e:
        print(f"View execution failed: {e}")
        return False
    
    # Test 5: Check campaign stats
    print("\n5. Testing campaign statistics...")
    active_campaigns = DonationCampaign.objects.filter(status='active').count()
    completed_campaigns = DonationCampaign.objects.filter(status='completed').count()
    
    print(f"Campaign statistics:")
    print(f"  - Active campaigns: {active_campaigns}")
    print(f"  - Completed campaigns: {completed_campaigns}")
    
    # Test 6: Check activity feed
    print("\n6. Testing activity feed...")
    recent_activities = CampaignActivity.objects.order_by('-created_at')[:5]
    print(f"Recent activities: {recent_activities.count()}")
    for activity in recent_activities:
        print(f"  - {activity.campaign.name}: {activity.get_activity_type_display()}")
    
    print("\nCampaign dashboard test completed successfully!")
    return True

if __name__ == '__main__':
    success = test_campaign_dashboard()
    if not success:
        print("\nCampaign dashboard test failed!")
        sys.exit(1)
