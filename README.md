# --- README.md ---

# Django Blog API

A Django REST Framework project for managing blog posts and categories with JWT authentication.

## Features

- User registration and JWT authentication
- CRUD operations for blog posts and categories
- Slug-based URLs
- Dynamic pagination
- Permissions: only authors can update/delete their posts

## Installation

1. Clone the repository:
```bash
git clone <YOUR_REPO_URL>
cd <YOUR_PROJECT_FOLDER>
```
2. Install Pipenv if not already installed:

```bash
pip install pipenv
```
3. Create a Pipenv environment and install dependencies:
```bash
pipenv install django==6.0.1 djangorestframework==3.15.0 djangorestframework-simplejwt==6.2.0 drf-spectacular==0.27.2 mysqlclient==2.1.1 django-cors-headers==4.3.0
```

4. Activate the Pipenv shell:
```bash
pipenv shell
```

5. Apply migrations and create a superuser (optional):
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```
