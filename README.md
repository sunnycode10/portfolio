# SunnyCode Portfolio

A premium, Django-based portfolio website for SunnyCode (Sunday Emmanuel Emenike).

## Tech Stack
- **Backend**: Django 5.x
- **Frontend**: Tailwind CSS, Alpine.js
- **Database**: SQLite (Development)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sunnycode
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Node Dependencies (for Tailwind)**
   ```bash
   npm install
   ```

4. **Apply Migrations**
   ```bash
   python3 manage.py migrate
   ```

5. **Populate Initial Data**
   ```bash
   python3 manage.py populate_data
   ```

6. **Build CSS**
   ```bash
   npm run build:css
   ```

7. **Run Server**
   ```bash
   python3 manage.py runserver
   ```

## Admin Panel
Access the admin panel at `/admin`.
Create a superuser first:
```bash
python3 manage.py createsuperuser
```

## Features
- **Dynamic Content**: Manage Projects, Skills, and Experience via Admin.
- **Blog**: Full blog functionality with Markdown support (planned).
- **Contact Form**: Integrated with Django backend.
- **Responsive Design**: Mobile-first approach using Tailwind CSS.
