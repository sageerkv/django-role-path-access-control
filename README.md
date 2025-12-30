# Django Role & Path-Based Access Control System

This is a backend-only Django REST API project that implements a simple **role and path-based permission system**.

Permissions control who can **view, add, edit, or delete Teams**.  
All access rules are enforced strictly by the backend.

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt

# Create migrations (IMPORTANT ORDER)
python manage.py makemigrations audit
python manage.py makemigrations

# Apply migrations
python manage.py migrate


# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

🛠 Admin Setup (Required)

Open admin panel

http://127.0.0.1:8000/admin/


Login using superuser credentials

Create a Path

Path Name: Team List

Status: Active

Create Roles

Admin

Manager

Viewer

Assign permissions in RolePathPermission
Example:

Path: Team List

can_view ✅

can_add ✅

can_edit ❌

can_delete ❌

Assign a Role to Users

📡 API Endpoints
Authentication
Method	Endpoint
POST	/api/token/
POST	/api/token/refresh/
POST	/api/logout/
Team APIs (Permission Controlled)
Method	Endpoint	Permission
GET	/api/teams/	Team List, view
POST	/api/teams/create/	Team List, add
PUT	/api/teams/<id>/update/	Team List, edit
DELETE	/api/teams/<id>/delete/	Team List, delete
🔒 Access Control

Each API checks permissions based on:

User → Role → Path → Action


Permissions are stored in the database and enforced by the backend only.

📌 Notes

Frontend cannot bypass permissions

Path names are case-sensitive

Permission changes apply immediately

📜 License

For educational and assessment use.


---





