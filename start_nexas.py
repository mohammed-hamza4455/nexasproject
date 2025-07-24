#!/usr/bin/env python
"""
NEXAS Application Startup Script
This script ensures all components are ready and starts the server.
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_nexas():
    """Setup and verify NEXAS application."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexas_project.settings')
    django.setup()
    
    print("🚀 Starting NEXAS Application...")
    print("=" * 50)
    
    # Check database
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
        print("✅ Database connection: OK")
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False
    
    # Ensure admin user exists
    try:
        from apps.accounts.models import User
        admin_user, created = User.objects.get_or_create(
            email='admin@nexas.com',
            defaults={
                'first_name': 'Admin',
                'last_name': 'User',
                'role': 'admin',
                'is_superuser': True,
                'is_staff': True,
            }
        )
        if created:
            admin_user.set_password('nexas123')
            admin_user.save()
            print("✅ Admin user created: admin@nexas.com")
        else:
            print("✅ Admin user exists: admin@nexas.com")
    except Exception as e:
        print(f"❌ User setup error: {e}")
        return False
    
    # Create test users
    try:
        test_users = [
            {'email': 'campaign@nexas.com', 'role': 'campaign', 'first_name': 'Campaign', 'last_name': 'Manager'},
            {'email': 'donation@nexas.com', 'role': 'donation', 'first_name': 'Donation', 'last_name': 'Manager'},
            {'email': 'volunteer@nexas.com', 'role': 'volunteer', 'first_name': 'John', 'last_name': 'Volunteer'},
        ]
        
        for user_data in test_users:
            user, created = User.objects.get_or_create(
                email=user_data['email'],
                defaults={
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                    'role': user_data['role'],
                }
            )
            if created:
                user.set_password('nexas123')
                user.save()
        
        print("✅ Test users ready")
    except Exception as e:
        print(f"⚠️  Test user setup warning: {e}")
    
    print("=" * 50)
    print("🎉 NEXAS Application Ready!")
    print()
    print("📋 Login Credentials:")
    print("   Admin: admin@nexas.com / nexas123")
    print("   Campaign Manager: campaign@nexas.com / nexas123") 
    print("   Donation Manager: donation@nexas.com / nexas123")
    print("   Volunteer: volunteer@nexas.com / nexas123")
    print()
    print("🌐 Access URLs:")
    print("   Login: http://localhost:8000/")
    print("   Admin Dashboard: http://localhost:8000/dashboard/admin/")
    print("   Django Admin: http://localhost:8000/admin/")
    print()
    print("🔥 Starting Development Server...")
    print("=" * 50)
    
    return True

if __name__ == '__main__':
    if setup_nexas():
        # Start the development server
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexas_project.settings')
        try:
            execute_from_command_line(['manage.py', 'runserver'])
        except KeyboardInterrupt:
            print("\n\n👋 NEXAS server stopped. Thanks for using NEXAS!")
    else:
        print("❌ Failed to start NEXAS. Please check the errors above.")
        sys.exit(1)
