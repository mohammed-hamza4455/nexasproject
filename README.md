# NEXAS Backend - Django Multi-Role Web Application

## Overview

NEXAS is a comprehensive Django backend system designed to support a multi-role web application with enterprise-grade security and performance. The system provides role-based access control for four distinct user types: Admin, Volunteer, Campaign Manager, and Donation Manager.

## Features

### 🔐 Authentication & Security
- **Custom User Model** with role-based permissions
- **Multi-role Authentication** (Admin, Volunteer, Campaign, Donation)
- **Role-based Middleware** for automatic access control
- **Session Security** with automatic timeout and tracking
- **Password Reset** functionality with email verification
- **Security Headers** and CSRF protection
- **Login History** tracking and audit logs

### 👥 User Management
- **Admin Dashboard** with comprehensive user management
- **User Creation** with role assignment
- **Profile Management** with extended user information
- **Account Locking** after failed login attempts
- **User Analytics** and reporting

### 📊 Dashboard System
- **Admin Dashboard** - System management and analytics
- **Volunteer Dashboard** - Task management and activity tracking
- **Campaign Dashboard** - Campaign management and metrics
- **Donation Dashboard** - Financial management and reporting

### 🔧 Technical Features
- **Django REST Framework** integration
- **PostgreSQL** support for production
- **Redis** integration for caching and sessions
- **Celery** support for background tasks
- **Comprehensive Logging** and error handling
- **API Endpoints** for AJAX functionality
- **Responsive Design** with Bootstrap 5

## Project Structure

```
nexas_backend/
├── nexas_project/              # Main Django project
│   ├── settings.py            # Django settings with environment variables
│   ├── urls.py                # Root URL configuration
│   ├── wsgi.py                # WSGI configuration
│   └── asgi.py                # ASGI configuration
├── apps/                      # Django applications
│   ├── accounts/              # User authentication and management
│   │   ├── models.py          # Custom User model with roles
│   │   ├── views.py           # Authentication views
│   │   ├── forms.py           # Authentication forms
│   │   ├── middleware.py      # Role-based access middleware
│   │   ├── permissions.py     # Custom permissions and mixins
│   │   └── management/        # Management commands
│   ├── admin_dashboard/       # Admin functionality
│   ├── volunteer_dashboard/   # Volunteer management
│   ├── campaign_dashboard/    # Campaign management
│   └── donation_dashboard/    # Donation management
├── templates/                 # HTML templates
├── static/                    # Static files (CSS, JS, images)
├── requirements.txt           # Python dependencies
└── manage.py                  # Django management script
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL (for production)
- Redis (optional, for caching)

### 1. Clone and Setup Virtual Environment
```bash
git clone <repository-url>
cd nexas_backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your settings
# Set SECRET_KEY, database credentials, email settings, etc.
```

### 4. Database Setup
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py create_superuser
```

### 5. Collect Static Files
```bash
python manage.py collectstatic
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## User Roles & Permissions

### Admin
- **Full System Access** - Complete control over all features
- **User Management** - Create, update, delete users
- **System Settings** - Configure application settings
- **Analytics & Reports** - Access to all system analytics
- **Audit Logs** - View all system activities

### Volunteer
- **Task Management** - View and update assigned tasks
- **Activity Logging** - Log volunteer hours and activities
- **Report Submission** - Submit volunteer reports
- **Profile Management** - Update personal information

### Campaign Manager
- **Campaign Management** - Create and manage campaigns
- **Goal Setting** - Set and track campaign goals
- **Volunteer Assignment** - Assign volunteers to campaigns
- **Performance Tracking** - Monitor campaign metrics

### Donation Manager
- **Donation Processing** - Manage donation records
- **Donor Management** - Maintain donor information
- **Financial Reports** - Generate financial reports
- **Receipt Generation** - Create donation receipts

## API Endpoints

### Authentication
- `POST /accounts/login/` - User login
- `POST /accounts/logout/` - User logout
- `POST /accounts/password-reset/` - Password reset request

### User Management (Admin Only)
- `GET /accounts/users/` - List users
- `POST /accounts/user/create/` - Create user
- `PUT /accounts/user/{id}/update/` - Update user
- `DELETE /accounts/user/{id}/delete/` - Delete user

### Dashboard APIs
- `GET /dashboard/admin/api/stats/` - Admin dashboard statistics
- `GET /dashboard/volunteer/api/stats/` - Volunteer dashboard statistics
- `GET /dashboard/campaign/api/stats/` - Campaign dashboard statistics
- `GET /dashboard/donation/api/stats/` - Donation dashboard statistics

## Security Features

### Authentication Security
- Password complexity requirements
- Account lockout after failed attempts (5 attempts = 30-minute lock)
- Session timeout after inactivity
- CSRF protection on all forms
- Secure cookie settings

### Authorization
- Role-based access control middleware
- Permission decorators and mixins
- URL-level access restrictions
- Object-level permissions

### Security Headers
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- X-XSS-Protection: 1; mode=block
- Content Security Policy
- HSTS headers (production)

## Default Credentials

After running the `create_superuser` command, the default admin credentials are:
- **Email:** admin@nexas.com
- **Password:** Admin@123
- **Role:** Admin

*Note: Change these credentials immediately in production!*

## Development Guidelines

### Code Style
- Follow PEP 8 standards
- Use Django best practices
- Include docstrings for all functions and classes
- Implement proper error handling

### Testing
```bash
# Run tests
python manage.py test

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### Database Migrations
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

## Production Deployment

### Environment Variables
Set the following in production:
- `DEBUG=False`
- `SECRET_KEY=<strong-secret-key>`
- Database credentials
- Email server settings
- `ALLOWED_HOSTS=<your-domain>`

### Database
Use PostgreSQL in production:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nexas_production',
        'USER': 'nexas_user',
        'PASSWORD': 'secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files
Configure static file serving:
```bash
python manage.py collectstatic
```

### Web Server
Use Gunicorn with Nginx:
```bash
gunicorn nexas_project.wsgi:application
```

## Monitoring & Logging

### Logging
The application logs to `logs/django.log` with the following levels:
- DEBUG: Development information
- INFO: General information
- WARNING: Warning messages
- ERROR: Error conditions
- CRITICAL: Critical errors

### Audit Trail
All user actions are logged in the `AuditLog` model for compliance and security monitoring.

## Support & Documentation

### Common Commands
```bash
# Create new Django app
python manage.py startapp app_name

# Database shell
python manage.py dbshell

# Django shell
python manage.py shell

# Check for issues
python manage.py check
```

### Troubleshooting

#### Common Issues:
1. **Migration errors**: Reset migrations if needed
2. **Static files not loading**: Run `collectstatic`
3. **Permission denied**: Check file permissions
4. **Database connection**: Verify database settings

#### Getting Help:
- Check Django documentation
- Review error logs in `logs/django.log`
- Use Django debug toolbar in development

## License

This project is proprietary software. All rights reserved.

## Contributing

Please follow the established coding standards and create pull requests for any changes.

---

**NEXAS Team**  
Version: 1.0.0  
Last Updated: 2025
