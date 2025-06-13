# Django User Authentication Project

This Django project implements a **user authentication system** with:
- Custom user model
- Registration, login, and logout views
- Login-required homepage
- `django-crispy-forms` with Bootstrap 5 for styling

## 📦 Requirements

- Python 3.8+
- Django 4+
- crispy-forms and Bootstrap 5

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your_repo_url>
cd <project_folder>
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4.Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5 . Run Django Server
```bash
python manage.py runserver
```