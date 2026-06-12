# RBAC Dashboard

A Django web app with Role-Based Access Control (RBAC). Supports two user roles — **Admin** (full CRUD on project data) and **Normal User** (read-only access). Features login/logout, a responsive sidebar with dropdown navigation, and a clean UI built with Tailwind CSS and Alpine.js.

## Features

- Login and logout authentication
- Role-based access control using Django Groups
- Admin can add, edit, and delete project data
- Normal User can only view project data
- Responsive sidebar with collapsible dropdown and hamburger toggle
- Clean modern UI with Tailwind CSS and Alpine.js

## User Roles

| Role | Access |
|------|--------|
| Admin | Full CRUD on projects |
| Normal User | Read-only access |

## Tech Stack

- Python / Django
- SQLite
- Tailwind CSS
- Alpine.js

## Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

1. Clone the repository
    ```bash
    git clone https://github.com/<your-username>/rbac_dashboard.git
    cd rbac_dashboard
    ```

2. Create and activate a virtual environment
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install dependencies
    ```bash
    pip install django
    ```

4. Run migrations
    ```bash
    python manage.py migrate
    ```

5. Create a superuser
    ```bash
    python manage.py createsuperuser
    ```

6. Run the server
    ```bash
    python manage.py runserver
    ```

7. Visit `http://127.0.0.1:8000`

## Setting Up User Roles

1. Go to `http://127.0.0.1:8000/admin`
2. Create two groups: `admin` and `NormalUser`
3. Create users and assign them to the appropriate group
