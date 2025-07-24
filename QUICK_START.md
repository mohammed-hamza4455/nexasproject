# 🚀 NEXAS Quick Start Guide

## Method 1: Super Simple (Recommended)

Run these commands exactly:

```bash
cd C:\Users\admin\Desktop\nexas_structure\nexas_backend
venv_new\Scripts\activate
pip install Django
python manage_minimal.py migrate
python manage_minimal.py create_superuser
python manage_minimal.py runserver
```

Then go to: http://127.0.0.1:8000/

## Method 2: If Method 1 Fails

Install packages one by one:

```bash
cd C:\Users\admin\Desktop\nexas_structure\nexas_backend
venv_new\Scripts\activate

# Install minimal requirements
pip install Django==4.2.7
pip install djangorestframework

# Try running
python manage_minimal.py migrate
python manage_minimal.py runserver
```

## Method 3: Create Fresh Environment

If nothing works, start completely fresh:

```bash
cd C:\Users\admin\Desktop\nexas_structure\nexas_backend

# Create new environment
python -m venv fresh_env
fresh_env\Scripts\activate

# Install only Django
pip install Django==4.2.7

# Run minimal version
python manage_minimal.py migrate
python manage_minimal.py runserver
```

## Login Details

- **URL:** http://127.0.0.1:8000/
- **Username:** admin@nexas.com  
- **Password:** Admin@123

## What to Expect

1. **Login Page** - Beautiful login interface
2. **Admin Dashboard** - Basic admin panel
3. **User Management** - Create and manage users

---

**Note:** The `manage_minimal.py` uses a simplified configuration that avoids dependency issues.
