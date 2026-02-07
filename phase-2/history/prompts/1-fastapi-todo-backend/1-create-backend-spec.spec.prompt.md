---
id: 3
title: Create FastAPI Todo Backend Spec
stage: spec
date: 2026-02-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: fastapi-todo-backend
branch: 1-fastapi-todo-backend
user: Claude
command: /sp.specify
labels: [spec, backend, fastapi, todo, authentication]
links:
  spec: specs/1-fastapi-todo-backend/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/1-fastapi-todo-backend/spec.md
  - specs/1-fastapi-todo-backend/checklists/requirements.md
tests:
---

## Prompt

```
# SP.spec.md – Backend Specification (FastAPI Todo Application)

I want you to generate a **fully functional backend** for a **Todo application** using **FastAPI**, **SQLAlchemy**, **PostgreSQL / Neon DB**, and **JWT authentication**. The backend must follow **SP.spec.md standards** for project specification. It should be **ready-to-run, modular, and secure**, using **UV package manager** for dependency management.

---

## **Project Overview**

**Backend Name:** todo_app_backend
**Framework:** FastAPI
**Database:** PostgreSQL / Neon DB
**Authentication:** JWT token (7-day expiry)
**Password Hashing:** Passlib (bcrypt)
**Dependency Management:** UV package manager (`uv init`, `uv add ...`)
**Port:** `localhost:8000`

**Key Features:**
1. User authentication (register, login, fetch current user)
2. JWT token-based authorization (Bearer token)
3. CRUD operations for Todos (user-specific)
4. Secure API endpoints with ownership enforcement
5. Modular and scalable structure
6. Ready-to-run with environment variable configuration

---

## **Folder Structure**

```

backend/
├─ app/
│  ├─ main.py              # FastAPI app initialization, route registration
│  ├─ auth.py              # User registration, login, JWT token creation
│  ├─ models.py            # SQLAlchemy models: User, Todo
│  ├─ crud.py              # CRUD functions for User and Todo
│  ├─ database.py          # DB connection and session creation
│  ├─ config.py            # Environment variable handling
│  └─ dependencies.py      # Dependency injection (DB session, current user)
├─ requirements.txt        # Python dependencies (for UV)
└─ .env                    # DB URL, JWT secret key, token expiry

```

---

## **Backend Specifications**

### **1. Authentication**

**Endpoints:**

- `POST /auth/register`
  - Input: `{ username, email, password }`
  - Validation: email format, password min 6 chars, username unique
  - Password stored hashed
  - Output: JWT token (Bearer, 7-day expiry)

- `POST /auth/login`
  - Input: `{ email, password }`
  - Validation: check user exists, verify password hash
  - Output: JWT token (Bearer, 7-day expiry)

- `GET /auth/me`
  - Input: Authorization header (Bearer token)
  - Output: Current logged-in user object
  - Protected route: JWT required

**JWT Logic:**
- Algorithm: HS256
- Secret key: from `.env` (`JWT_SECRET`)
- Expiry: 7 days
- Token contains: `user_id`, `username`, `email`, `exp`

---

### **2. Todos CRUD**

**Endpoints:**

- `POST /todos/` → Create Todo
  - Input: `{ title, description }`
  - Validation: title required
  - Assign `owner_id` from current user
  - Output: Created todo object

- `GET /todos/` → Get all Todos (user-specific)
  - Returns all todos where `owner_id == current user id`

- `GET /todos/{id}` → Get single Todo
  - Validate ownership (`owner_id`)
  - Returns todo object
  - Error: 404 if not found, 401 if unauthorized

- `PUT /todos/{id}` → Update Todo
  - Input: `{ title?, description?, completed? }`
  - Validate fields if provided
  - Update todo in DB
  - Returns updated todo

- `DELETE /todos/{id}` → Delete Todo
  - Validate ownership
  - Delete todo
  - Returns success message

**Business Rules:**
- Users can only access their own todos
- Completed is boolean, default `False`
- Owner cannot be changed
- Timestamp fields: `created_at`, `updated_at`
- Proper HTTP status codes: 200, 201, 401, 404, 400

---

### **3. Database Models (models.py)**

**User:**
- id: UUID / primary key
- username: string, unique
- email: string, unique
- password_hash: string
- todos: relationship → Todo

**Todo:**
- id: UUID / primary key
- title: string, required
- description: string, optional
- completed: boolean, default False
- owner_id: foreign key → User.id
- created_at: datetime
- updated_at: datetime

---

### **4. Dependencies**

**dependencies.py**
- `get_db()`: yields DB session
- `get_current_user(token: str)`: decodes JWT, returns user
- All endpoints requiring authentication use `Depends(get_current_user)`

---

### **5. Environment Variables (.env)**

- `DATABASE_URL` → PostgreSQL / Neon DB connection string
- `JWT_SECRET` → Secret key for token
- `ACCESS_TOKEN_EXPIRE_DAYS` → 7
- `UV_PORT` → 8000

---

### **6. UV Package Manager Integration**

**Commands:**
1. `uv init` → initialize project
2. `uv add fastapi sqlalchemy psycopg2-binary passlib python-jose pydantic uvicorn`
3. `uv run app/main.py --reload` → start backend server

---

### **7. Error Handling**

- 401 Unauthorized → JWT missing/invalid
- 404 Not Found → Todo or user does not exist
- 400 Bad Request → Validation errors
- 422 Unprocessable → Pydantic schema validation errors

---

### **8. Security**

- Passwords stored hashed (bcrypt)
- JWT token with expiry
- All `/todos` routes protected
- Users cannot access others' todos
- No sensitive info returned in responses

---

### **9. Output Expectations**

- Ready-to-run backend project
- Fully working JWT auth
- CRUD for todos
- Modular code: auth, crud, models, main
- UV package manager integrated
- Clear separation: business logic, database logic, authentication
- Proper documentation/comments for SP.spec.md

---

Generate **all backend files** (`main.py`, `auth.py`, `crud.py`, `models.py`, `database.py`, `config.py`, `dependencies.py`) fully functional, ready-to-run, with JWT auth, todo CRUD, and PostgreSQL/Neon DB integration. Ensure **SP.spec.md compliance** for backend.
```

---

## Response snapshot

Created a comprehensive specification for the FastAPI Todo application backend with detailed functional requirements covering authentication, todo management, security, and data management. The specification includes user scenarios, acceptance criteria, edge cases, success metrics, and key entities. A validation checklist was also created to ensure the specification meets quality standards.

## Outcome

- ✅ Impact: Created complete backend specification with functional requirements, security considerations, and success criteria
- 🧪 Tests: No tests created as this is a specification document
- 📁 Files: Created specs/1-fastapi-todo-backend/spec.md and specs/1-fastapi-todo-backend/checklists/requirements.md
- 🔁 Next prompts: Proceed to planning phase with /sp.plan to design implementation approach
- 🧠 Reflection: The specification clearly defines the backend requirements while maintaining focus on user value and business needs without implementation details

## Evaluation notes (flywheel)

- Failure modes observed: None - successful creation of specification document
- Graders run and results (PASS/FAIL): N/A for specification creation
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin planning implementation with /sp.plan