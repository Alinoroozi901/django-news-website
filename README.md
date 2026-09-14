# 📰 Django News Website

A full-featured news and article platform built with Django, focusing on clean backend architecture using Class-Based Views and custom mixins.

\---

## Features

* 🔐 **Authentication System** — Register, Login, Logout
* 📧 **Password Reset** — Forgot password sends a reset email automatically
* 📝 **Articles** — Create, read, update and delete articles
* 💬 **Comments** — Comment on any article in its dedicated detail page
* 🔍 **Search** — Search articles by title and body with multi-word support
* 👍 **Likes \& Views** — Track article engagement
* 🛡️ **Permissions** — Only authors and staff can edit or delete articles
* 🧩 **Custom Mixins** — Reusable login and permission logic across all views

\---

## Built With

* **Python** 3.11
* **Django** 5.x
* **SQLite** (development database)
* **environs** — for secure environment variable management

\---

## Setup \& Installation

1. **Clone the repository**

```bash
git clone https://github.com/Alinoroozi901/your-repo-name.git
cd your-repo-name
```

2. **Create a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create your `.env` file** in the same folder as `manage.py`

```
DEBUG=True
SECRET\_KEY=your-secret-key-here
```

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Start the server**

```bash
python manage.py runserver
```

\---

## Project Structure

```
news/
├── manage.py
├── .env
├── django\_project/          ← main project config
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── accounts/                ← user authentication app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── articles/                ← articles \& comments app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── mixins.py
│   ├── urls.py
│   └── admin.py
├── pages/                   ← static pages app (home, etc)
│   ├── views.py
│   └── urls.py
├── staticfiles/
└── templates/
    ├── base.html
    ├── home.html
    ├── article\_list.html
    ├── article\_detail.html
    ├── article\_create.html
    ├── article\_edit.html
    ├── article\_delete.html
    └── registration/
        ├── login.html
        ├── signup.html
        ├── password\_reset\_form.html
        ├── password\_reset\_done.html
        ├── password\_reset\_confirm.html
        └── password\_reset\_complete.html
```

\---

## About the Developer

Hi! I'm Ali, a 15-year-old self-taught Django developer from Iran. I started coding at 14 and I'm passionate about building real web applications and growing as a backend developer.

Feel free to reach out or connect!

\---

## Note

This project is part of my learning journey. I am always open to feedback, suggestions, and collaboration!

