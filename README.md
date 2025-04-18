Corporate Resume Builder - Developer 3 Modules
Overview
This repository contains the Employee, Project, and Technology/Tools modules (Developer 3) integrated with the Admin Page module (Developer 1) for the Corporate Resume Generator SaaS platform.
Setup

Clone: git clone https://github.com/yourusername/corporate-resume-generator.git

Install dependencies: pip install -r requirements.txt

Set up MySQL: CREATE DATABASE resume_db;

Create .env:
SECRET_KEY=your-secret-key
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
admin_page (Developer 1): Company management (name, email, plan_type, etc.).

Projects

Views:
project_list: Lists active and deleted projects at /projects/.
project_create: Creates projects at /projects/create/ with Select2 dropdowns for technologies/tools.
project_update: Updates projects at /projects/<pk>/update/.
project_delete: Soft deletes at /projects/<pk>/delete/.
project_restore: Restores at /projects/<pk>/restore/.
project_permanent_delete: Permanently deletes at /projects/<pk>/permanent_delete/.


Fields: Name, Description, Technologies (multi-select), Tools (multi-select), Roles and Responsibilities, Start Date, End Date, Status (Active/Closed).
Employee Mapping: Assign multiple employees to projects (many-to-many).
Multi-Select UX: Technologies, tools, and employees use Select2 for selecting specific options (e.g., only Python and Git).
Data for Resumes: Projects store specific technologies (e.g., Python, Java) and tools (e.g., Git, Jira) in many-to-many fields, queryable via project.technologies.all() and project.tools.all().
Soft Delete, Restore, and Permanent Delete:
Active projects shown with "Edit" and "Delete" buttons.
Deleted projects shown with "Restore" and "Permanent Delete" buttons.
Duplicate name errors suggest checking deleted projects.


Used in employee form dropdowns (projects field) and resume generation.

Employees

Views:
employee_list: Lists active and deleted employees at /employees/.
employee_create: Creates employees at /employees/create/ with Select2 dropdowns for skills/projects.
employee_update: Updates employees at /employees/<pk>/update/.
employee_delete: Soft deletes at /employees/<pk>/delete/.
employee_restore: Restores at /employees/<pk>/restore/.
employee_permanent_delete: Permanently deletes at /employees/<pk>/permanent_delete/.


Fields: Name, Designation, Summary, Skills (Coding, Tools), Projects.
Data for Resumes: Employees link to projects via employee.projects, providing access to project-specific technologies/tools.
Used in project employee mappings.



Soft Delete, Restore, and Permanent Delete:
Active records shown with "Edit" and "Delete" buttons.
Deleted records shown with "Restore" and "Permanent Delete" buttons.
Duplicate name errors suggest checking deleted records.








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

