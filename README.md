# Django News Website

A full-featured news and article platform built with Django, focusing on clean backend architecture using Class-Based Views and custom mixins.

---

## Features

- Authentication System — Register, Login, Logout
- Password Reset — Forgot password sends a reset email automatically
- Articles — Create, read, update and delete articles
- Comments — Comment on any article in its dedicated detail page
- Search — Search articles by title and body with multi-word support
- Likes — Like and unlike articles, each user can only like once
- Views — Track article views, each user counted once
- Permissions — Only authors and staff can edit or delete articles
- Custom Mixins — Reusable login and permission logic across all views

---

## Built With

- Python 3.11
- Django 5.x
- SQLite (development database)
- environs — for secure environment variable management

---

## Setup & Installation

1. Clone the repository
```bash
git clone https://github.com/Alinoroozi901/django-news-website.git
cd django-news-website
```

2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create your `.env` file next to `manage.py`
DEBUG=True
SECRET_KEY=your-secret-key-here

5. Run migrations
```bash
python manage.py migrate
```

6. Start the server
```bash
python manage.py runserver
```

---

## Project Structure
```
news/
├── manage.py
├── .env
├── django_project/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
├── accounts/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── admin.py
├── articles/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── mixins.py
│ ├── urls.py
│ └── admin.py
├── pages/
│ ├── views.py
│ └── urls.py
├── staticfiles/
└── templates/
├── base.html
├── home.html
├── article_list.html
├── article_detail.html
├── article_create.html
├── article_edit.html
├── article_delete.html
└── registration/
├── login.html
├── signup.html
├── password_reset_form.html
├── password_reset_done.html
├── password_reset_confirm.html
└── password_reset_complete.html
```
---

## About the Developer

Hi! I'm Ali, a 15-year-old self-taught Django developer from Iran. I started coding at 14 and I'm passionate about building real web applications and growing as a backend developer.

Feel free to reach out or connect!

GitHub: https://github.com/Alinoroozi901

---

## Note

This project is part of my learning journey. I am always open to feedback, suggestions, and collaboration!

