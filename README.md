Corporate Resume Builder - Developer 3 Modules
Overview
This repository contains the Employee, Project, and Technology/Tools modules (Developer 3) integrated with the Admin Page module (Developer 1) for the Corporate Resume Generator SaaS platform.
Setup

Clone: git clone https://github.com/aaarrvind/corporate-resume-generator.git

Install dependencies: pip install -r requirements.txt

Set up MySQL: CREATE DATABASE resume_db;


Edit the database in settings 
DB_NAME=resume_db
DB_USER=your_username
DB_PASSWORD=your_password


Update backend/settings.py.

Run migrations: python manage.py migrate

Create superuser: python manage.py createsuperuser

Run server: python manage.py runserver


Modules

employees: CRUD for employee data (name, designation, skills, projects), linked to a company.
projects: CRUD for projects (name, technologies, dates, employee mappings), linked to a company.
technologies: System-wide master lists for coding languages and tools, managed by Company Admins.
admin_page: Company management (name, email, plan_type, etc.).








Setup Test Data:
Create a company:
from admin_page.models import Company
from datetime import date
Company.objects.create(
    name='Test Corp',
    email='testcorp@example.com',
    password='securepassword123',
    plan_type='Basic',
    subscription_start=date(2025, 4, 1),
    subscription_end=date(2026, 4, 1),
    is_active=True
)


Add technologies/tools via /technologies/coding-languages/, /technologies/tools/, or /admin/.

Add projects and employees via /projects/ and /employees/.



Notes:
Filter by company and is_deleted=False for active data.
Use /admin/ for quick data entry.
Project technologies/tools are set in /projects/create/ or /projects/<pk>/update/ using Select2 dropdowns.



Notes

Uses Django’s User model until Developer 2’s authentication is ready.
URLs: /employees/, /projects/, /technologies/coding-languages/, /technologies/tools/.
Run python manage.py check to verify setup.

