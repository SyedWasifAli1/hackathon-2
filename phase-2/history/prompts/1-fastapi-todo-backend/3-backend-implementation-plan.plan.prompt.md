---
id: 5
title: Backend Implementation Plan
stage: plan
date: 2026-02-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: fastapi-todo-backend
branch: 001-fastapi-todo-backend
user: Claude
command: /sp.plan
labels: [plan, backend, fastapi, todo, architecture]
links:
  spec: specs/001-fastapi-todo-backend/spec.md
  plan: specs/001-fastapi-todo-backend/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-fastapi-todo-backend/plan.md
  - specs/001-fastapi-todo-backend/research.md
  - specs/001-fastapi-todo-backend/data-model.md
  - specs/001-fastapi-todo-backend/contracts/openapi.yaml
  - specs/001-fastapi-todo-backend/quickstart.md
tests:
---

## Prompt

```
# Backend Execution Plan – Todo Application

I want you to generate a **complete backend execution plan** for a **production-ready Todo application** using **FastAPI**, **SQLModel**, **JWT authentication**, and **Neon Serverless PostgreSQL**, managed via the **UV package manager**.

This plan MUST strictly and mandatorily use the following skills. Each skill must be applied in implementation, not just mentioned.

## Mandatory Skills to Use
- uv-initialization
- sqlmodel-task-models
- fastapi-jwt-auth
- neon-async-db
- secure-task-crud
- sqlmodel-db
- fastapi-jwt

Failure to use any of the above skills is NOT acceptable.

---

## 1. Environment & Package Setup (Skill: uv-initialization)

### Objective
Initialize a modern Python backend using UV as the package and environment manager.

### Tasks
- Initialize project using `uv init`
- Create backend directory structure:
  - `backend/app/`
- Install dependencies using `uv add`:
  - fastapi
  - uvicorn
  - sqlmodel
  - asyncpg
  - python-jose
  - passlib[bcrypt]
  - python-dotenv
- Ensure UV lockfile is generated
- Configure `.env` file with:
  - DATABASE_URL (Neon PostgreSQL)
  - JWT_SECRET
  - JWT_ALGORITHM=HS256
  - ACCESS_TOKEN_EXPIRE_DAYS=7

### Output
- Backend runnable via:
  `uv run uvicorn app.main:app --reload`

---

## 2. Database Configuration (Skills: sqlmodel-db, neon-async-db)

### Objective
Setup an **async SQLModel + Neon PostgreSQL** database layer.

### Tasks
- Create `database.py`
- Configure async engine using Neon DB connection string
- Use `asyncpg` driver
- Implement `AsyncSession` with dependency injection
- Create database initialization logic (metadata.create_all)
- Ensure async-safe session lifecycle

### Rules
- All DB operations MUST be async
- No synchronous DB calls allowed

---

## 3. Data Models Definition (Skill: sqlmodel-task-models)

### Objective
Define clean, relational SQLModel schemas.

### Models

#### User Model
- id (UUID, Primary Key)
- username (string, unique, indexed)
- email (string, unique, indexed)
- password_hash (string)
- created_at (datetime)
- Relationship: one-to-many with Todo

#### Todo Model
- id (UUID, Primary Key)
- title (string, required)
- description (string, optional)
- completed (boolean, default False)
- owner_id (UUID, Foreign Key → User.id)
- created_at (datetime)
- updated_at (datetime)

### Rules
- Use SQLModel ORM
- Relationships must be defined
- Index user_id for performance

---

## 4. Authentication System (Skills: fastapi-jwt-auth, fastapi-jwt)

### Objective
Implement **secure JWT-based authentication**.

### JWT Rules
- Token type: Bearer
- Algorithm: HS256
- Expiry: 7 days
- Secret from environment variables

### Auth Features
- Register user:
  - Hash password using bcrypt
  - Prevent duplicate email
  - Auto-issue JWT on success
- Login user:
  - Validate credentials
  - Issue JWT
- Get current user:
  - Decode JWT
  - Fetch user from DB
  - Reject invalid/expired tokens

### Security Rules
- Passwords NEVER returned
- Invalid tokens → HTTP 401
- Expired tokens → HTTP 401

---

## 5. Secure Todo CRUD Logic (Skill: secure-task-crud)

### Objective
Implement **user-isolated Todo CRUD operations**.

### CRUD Operations

#### Create Todo
- Requires JWT
- Assign owner_id from token
- Validate title

#### Read Todos
- Return only todos owned by authenticated user

#### Read Single Todo
- Verify ownership
- 404 if not found
- 403 if not owner

#### Update Todo
- Partial updates allowed
- Ownership validation required

#### Delete Todo
- Ownership validation required
- Hard delete

### Rules
- No cross-user access allowed
- All operations protected via JWT

---

## 6. Dependency Management Layer

### Objective
Centralize reusable dependencies.

### Dependencies
- `get_async_db_session`
- `get_current_user_from_jwt`

### Rules
- Must use FastAPI `Depends`
- Must be reusable across routes

---

## 7. API Routing Structure

### Auth Routes
- POST `/auth/register`
- POST `/auth/login`
- GET `/auth/me`

### Todo Routes
- POST `/todos/`
- GET `/todos/`
- GET `/todos/{id}`
- PUT `/todos/{id}`
- DELETE `/todos/{id}`

### Global Rules
- All `/todos` routes require JWT
- Proper HTTP status codes enforced

---

## 8. Business Rules & Validation

- JWT mandatory for protected routes
- Users can only see and modify their own data
- Token expiry enforced
- Async-only DB access
- Clean error handling (401, 403, 404, 422)

---

## 9. Final Deliverables

- Fully working FastAPI backend
- UV-managed environment
- Async Neon PostgreSQL integration
- Secure JWT authentication
- SQLModel ORM
- Clean modular structure:
  - main.py
  - auth.py
  - models.py
  - crud.py
  - database.py
  - dependencies.py
- Production-ready and scalable

---

## Execution Instruction

Generate backend code strictly following this plan.
All listed skills MUST be used.
The backend must run successfully without manual fixes.
```

## Response snapshot

Created a comprehensive implementation plan for the FastAPI Todo application backend, including research, data model, API contracts, and quickstart guide. Applied all required skills (uv-initialization, sqlmodel-task-models, fastapi-jwt-auth, neon-async-db, secure-task-crud, sqlmodel-db, fastapi-jwt) in the planning process. Developed concrete deliverables including project structure, data models with relationships and validation rules, API contracts in OpenAPI format, and implementation guidelines.

## Outcome

- ✅ Impact: Complete backend implementation plan with all required components and skills
- 🧪 Tests: No tests created as this is a planning document
- 📁 Files: Created plan.md, research.md, data-model.md, contracts/openapi.yaml, quickstart.md
- 🔁 Next prompts: Proceed to task generation with /sp.tasks for implementation steps
- 🧠 Reflection: Plan comprehensively addresses all requirements with proper architecture

## Evaluation notes (flywheel)

- Failure modes observed: None - successful plan completion
- Graders run and results (PASS/FAIL): N/A for planning document
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Generate implementation tasks with /sp.tasks