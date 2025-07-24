# NEXAS Django Backend - Deployment Guide

## ✅ Installation Complete!

Your NEXAS Django backend is now successfully installed and ready to use.

### 🚀 Quick Start

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application:**
   - **Login Page:** http://127.0.0.1:8000/
   - **Admin Interface:** http://127.0.0.1:8000/admin/

### 🔑 Default Login Credentials

- **Email:** admin@nexas.com
- **Password:** Admin@123
- **Role:** Admin

### 📊 Available Dashboards

After logging in, you'll be automatically redirected to the appropriate dashboard:

- **Admin Dashboard:** `/dashboard/admin/` - Complete system management
- **Volunteer Dashboard:** `/dashboard/volunteer/` - Task and activity management
- **Campaign Dashboard:** `/dashboard/campaign/` - Campaign management
- **Donation Dashboard:** `/dashboard/donation/` - Financial management

### 🛠️ Development Commands

```bash
# Create new users
python manage.py createsuperuser

# Make migrations after model changes
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Check for issues
python manage.py check
```

### 🔧 Create Additional Users

1. Log in as admin at http://127.0.0.1:8000/
2. Navigate to **User Management** in the admin dashboard
3. Click **Add New User**
4. Fill in the details and assign roles:
   - **Admin:** Full system access
   - **Volunteer:** Task management
   - **Campaign:** Campaign management  
   - **Donation:** Financial management

### 🎯 Next Steps

1. **Test Login System:**
   - Try logging in with admin credentials
   - Test role-based dashboard redirection

2. **Create Test Users:**
   - Create users for each role type
   - Test dashboard access for each role

3. **Customize Templates:**
   - Modify templates in `templates/` directory
   - Update static files in `static/` directory

4. **Configure Email:**
   - Set up email settings in `.env` file
   - Test password reset functionality

### 🔒 Security Notes

- Change default admin password immediately
- Set up proper environment variables for production
- Configure HTTPS for production deployment
- Review security settings in `settings.py`

### 📁 Important Directories

- **Templates:** `templates/` - HTML templates
- **Static Files:** `static/` - CSS, JS, images
- **Apps:** `apps/` - Django applications
- **Settings:** `nexas_project/settings.py`

### 🐛 Troubleshooting

**Common Issues:**

1. **Migration Errors:**
   ```bash
   python manage.py makemigrations --empty appname
   python manage.py migrate
   ```

2. **Static Files Not Loading:**
   ```bash
   python manage.py collectstatic --clear
   ```

3. **Permission Errors:**
   - Check user roles in Django admin
   - Verify middleware configuration

### 🎉 Success!

Your NEXAS Django backend is now fully operational with:

✅ Multi-role authentication system  
✅ Role-based dashboard access  
✅ User management capabilities  
✅ Security middleware and logging  
✅ Responsive design templates  
✅ API endpoints for AJAX functionality

**Happy coding! 🚀**
