#!/usr/bin/env python
"""
Create sample data for campaign dashboard testing.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexas_project.settings')
django.setup()

from django.utils import timezone
from apps.accounts.models import User
from apps.donation_dashboard.models import DonationCampaign, CampaignActivity

def create_campaign_manager():
    """Create a campaign manager user."""
    
    # Create campaign manager if doesn't exist
    campaign_manager, created = User.objects.get_or_create(
        email='campaign@nexas.org',
        defaults={
            'first_name': 'Campaign',
            'last_name': 'Manager',
            'role': 'campaign',
            'is_active': True,
        }
    )
    
    if created:
        campaign_manager.set_password('nexas123')
        campaign_manager.save()
        print(f"Created campaign manager: {campaign_manager.email}")
    else:
        print(f"Campaign manager already exists: {campaign_manager.email}")
    
    return campaign_manager

def create_sample_activities():
    """Create sample campaign activities."""
    
    campaigns = DonationCampaign.objects.all()
    
    if not campaigns:
        print("No campaigns found. Please create campaigns first.")
        return
    
    activities_data = [
        {
            'activity_type': 'donation_received',
            'description': 'Received ₹10,000 donation from Raj Sharma',
        },
        {
            'activity_type': 'volunteer_joined',
            'description': 'Volunteer <strong>Mary Johnson</strong> joined campaign',
        },
        {
            'activity_type': 'milestone_reached',
            'description': 'Campaign reached 50% of fundraising goal',
        },
        {
            'activity_type': 'campaign_shared',
            'description': 'Campaign shared on social media platforms',
        },
        {
            'activity_type': 'report_generated',
            'description': 'Generated quarterly impact report',
        },
    ]
    
    created_count = 0
    for campaign in campaigns[:2]:  # Only first 2 campaigns
        for activity_data in activities_data:
            activity, created = CampaignActivity.objects.get_or_create(
                campaign=campaign,
                activity_type=activity_data['activity_type'],
                description=activity_data['description']
            )
            if created:
                created_count += 1
    
    print(f"Created {created_count} campaign activities")

def update_campaign_managers():
    """Assign campaign manager to campaigns."""
    
    try:
        campaign_manager = User.objects.get(email='campaign@nexas.org')
        
        # Update campaigns without managers
        campaigns_updated = DonationCampaign.objects.filter(
            manager__isnull=True
        ).update(manager=campaign_manager)
        
        print(f"Assigned campaign manager to {campaigns_updated} campaigns")
        
    except User.DoesNotExist:
        print("Campaign manager not found")

if __name__ == '__main__':
    print("Creating campaign dashboard sample data...")
    
    # Create campaign manager
    create_campaign_manager()
    
    # Update campaign managers
    update_campaign_managers()
    
    # Create sample activities
    create_sample_activities()
    
    print("Campaign dashboard sample data created successfully!")
