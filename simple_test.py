#!/usr/bin/env python
"""
Simple test to verify the donation dashboard template exists and loads.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexas_project.settings')
django.setup()

from django.template.loader import get_template
from apps.donation_dashboard.models import Donor, DonationCampaign
from apps.accounts.models import User

def test_template_loading():
    """Test if the new template loads correctly."""
    
    print("Testing template loading...")
    
    # Test 1: Check if template exists
    try:
        template = get_template('donation_dashboard/donor_dashboard_new.html')
        print("Template found: donation_dashboard/donor_dashboard_new.html")
    except Exception as e:
        print(f"Template not found: {e}")
        return False
    
    # Test 2: Check sample data
    donation_users = User.objects.filter(role='donation').count()
    donors = Donor.objects.count()
    campaigns = DonationCampaign.objects.filter(status='active').count()
    
    print(f"Sample data:")
    print(f"  - Donation users: {donation_users}")
    print(f"  - Donors: {donors}")
    print(f"  - Active campaigns: {campaigns}")
    
    # Test 3: Check if we can create context for template
    try:
        from django.template.context import RequestContext
        from django.test import RequestFactory
        
        # Create a mock request for proper context
        factory = RequestFactory()
        request = factory.get('/dashboard/donation/')
        
        # Sample context similar to what the view would create
        context = {
            'stats': {
                'total_donated': 10000.00,
                'donation_count': 5,
                'campaigns_supported': 2,
            },
            'recent_donations': [],
            'all_donations': [],
            'active_campaigns': DonationCampaign.objects.filter(status='active')[:5],
            'user': {'email': 'test@example.com'},
            'request': request,
        }
        
        # Try to render template with context
        rendered = template.render(context)
        print(f"Template rendered successfully ({len(rendered)} characters)")
        
        # Check if key elements are in the rendered HTML
        if 'Donator Dashboard' in rendered:
            print("Dashboard title found in template")
        if 'total_donated' in rendered or '10000' in rendered:
            print("Stats data found in template")
        if 'NEXAS' in rendered:
            print("Branding found in template")
            
        return True
        
    except Exception as e:
        print(f"Template rendering failed: {e}")
        return False

if __name__ == '__main__':
    success = test_template_loading()
    if success:
        print("\nTemplate test completed successfully!")
    else:
        print("\nTemplate test failed!")
