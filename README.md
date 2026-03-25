# Healthcare Backend API

A Django REST Framework backend for managing patients, doctors, and their mappings with JWT authentication and PostgreSQL.

## Setup Instructions

### 1. Install Python (3.10+)
Download from [python.org](https://www.python.org/downloads/).

### 2. Create & activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL
- Install PostgreSQL and create a database:
```sql
CREATE DATABASE healthcare_db;
```
- Update `.env` with your credentials:
```
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`.

---

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register (name, email, password) |
| POST | `/api/auth/login/` | Login → returns JWT tokens |

### Patients (Authenticated)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/patients/` | Add a new patient |
| GET | `/api/patients/` | List your patients |
| GET | `/api/patients/<id>/` | Get patient details |
| PUT | `/api/patients/<id>/` | Update patient |
| DELETE | `/api/patients/<id>/` | Delete patient |

### Doctors (Authenticated)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/doctors/` | Add a new doctor |
| GET | `/api/doctors/` | List all doctors |
| GET | `/api/doctors/<id>/` | Get doctor details |
| PUT | `/api/doctors/<id>/` | Update doctor |
| DELETE | `/api/doctors/<id>/` | Delete doctor |

### Patient-Doctor Mappings (Authenticated)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/mappings/` | Assign doctor to patient |
| GET | `/api/mappings/list/` | List all mappings |
| GET | `/api/mappings/<patient_id>/` | Doctors for a patient |
| DELETE | `/api/mappings/delete/<id>/` | Remove a mapping |

### Authentication Header
```
Authorization: Bearer <access_token>
```

---

## Tech Stack
- **Django 4.2** + **Django REST Framework**
- **PostgreSQL** (via psycopg2)
- **JWT Auth** (djangorestframework-simplejwt)
- **python-decouple** (env var management)
# WhatBytes-Django-Assignment
