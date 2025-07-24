#!/usr/bin/env python
"""
Test script to debug donation creation issues.
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexas_project.settings')
django.setup()

from apps.donation_dashboard.models import Donor, Donation, DonationCampaign
from decimal import Decimal
from django.utils import timezone
import uuid

def test_donation_creation():
    """Test creating a donation to debug the issue."""
    try:
        # Create or get a test donor
        donor, created = Donor.objects.get_or_create(
            email='test@example.com',
            defaults={
                'first_name': 'Test',
                'last_name': 'User',
                'donor_type': 'individual',
            }
        )
        print(f"Donor: {'Created' if created else 'Found'} - {donor}")
        
        # Generate transaction ID
        transaction_id = f"TX-{timezone.now().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:8].upper()}"
        print(f"Transaction ID: {transaction_id}")
        
        # Create donation
        donation = Donation.objects.create(
            donor=donor,
            campaign=None,
            amount=Decimal('1000.00'),
            currency='INR',
            payment_method='credit_card',
            is_anonymous=False,
            status='completed',
            transaction_id=transaction_id,
            source='website'
        )
        print(f"Donation created successfully: {donation}")
        
        # Try updating stats
        donor.update_donation_stats()
        print(f"Donor stats updated: Total donated = {donor.total_donated}")
        
        return True
        
    except Exception as e:
        print(f"Error creating donation: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_donation_creation()
    print(f"\nTest {'PASSED' if success else 'FAILED'}")
