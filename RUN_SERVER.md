# 🚀 How to Run NEXAS Server

## Step-by-Step Instructions

### 1. Open Command Prompt and Navigate to Project
```bash
cd C:\Users\admin\Desktop\nexas_structure\nexas_backend
```

### 2. Activate the New Virtual Environment
```bash
venv_new\Scripts\activate
```

You should see `(venv_new)` at the beginning of your prompt.

### 3. Install Required Packages (if not done already)
```bash
pip install Django==4.2.7 django-crispy-forms crispy-bootstrap5 djangorestframework
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Create Admin User (if not done already)
```bash
python manage.py create_superuser
```

### 6. Start the Server
```bash
python manage.py runserver
```

### 7. Access the Application
Open your browser and go to:
- **Login Page:** http://127.0.0.1:8000/
- **Admin Interface:** http://127.0.0.1:8000/admin/

### 8. Login Credentials
- **Email:** admin@nexas.com
- **Password:** Admin@123

## If You Get Errors

### "No module named 'django'"
Make sure you activated the virtual environment:
```bash
venv_new\Scripts\activate
```

### Migration Errors
```bash
python manage.py makemigrations
python manage.py migrate
```

### Virtual Environment Issues
If nothing works, create a fresh environment:
```bash
python -m venv fresh_venv
fresh_venv\Scripts\activate
pip install Django==4.2.7
python manage.py runserver
```

## Quick Test Commands

```bash
# Check Django is installed
python -c "import django; print(django.VERSION)"

# Check project structure
python manage.py check

# View all available commands
python manage.py help
```

---
**Note:** Always make sure you see `(venv_new)` or `(fresh_venv)` in your command prompt before running Django commands!
