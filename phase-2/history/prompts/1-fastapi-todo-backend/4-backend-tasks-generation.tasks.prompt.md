---
id: 6
title: Backend Tasks Generation
stage: tasks
date: 2026-02-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: fastapi-todo-backend
branch: 001-fastapi-todo-backend
user: Claude
command: /sp.tasks
labels: [tasks, backend, fastapi, todo, implementation]
links:
  spec: specs/001-fastapi-todo-backend/spec.md
  plan: specs/001-fastapi-todo-backend/plan.md
  tasks: specs/001-fastapi-todo-backend/tasks.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-fastapi-todo-backend/tasks.md
tests:
---

## Prompt

```
# SP.task.md
# Backend Task Breakdown – Todo Application

I want you to generate a **complete task-level breakdown** for implementing the backend of a **Todo application** using **FastAPI**, **SQLModel**, **JWT authentication**, **Neon async PostgreSQL**, and **UV package manager**.

These tasks must be **atomic**, **ordered**, and **directly executable** by Claude Code using Spec-Kit.
Each task MUST explicitly use one or more of the following skills.

## Mandatory Skills (Must Be Used)
- uv-initialization
- sqlmodel-task-models
- fastapi-jwt-auth
- neon-async-db
- secure-task-crud
- sqlmodel-db
- fastapi-jwt

Skipping or ignoring any skill is NOT allowed.

---

## 🧩 TASK GROUP 1: Project & Environment Setup
**Skills:** uv-initialization

### Task 1.1 – Initialize UV Project
- Run `uv init`
- Create `backend/` root
- Ensure UV environment is active

### Task 1.2 – Install Backend Dependencies
- Install via `uv add`:
  - fastapi
  - uvicorn
  - sqlmodel
  - asyncpg
  - python-jose
  - passlib[bcrypt]
  - python-dotenv
- Verify `uv.lock` is created

### Task 1.3 – Environment Configuration
- Create `.env`
- Add:
  - DATABASE_URL
  - JWT_SECRET
  - JWT_ALGORITHM=HS256
  - ACCESS_TOKEN_EXPIRE_DAYS=7

---

## 🧩 TASK GROUP 2: Database Layer
**Skills:** sqlmodel-db, neon-async-db

### Task 2.1 – Async Database Engine
- Create `database.py`
- Configure async SQLModel engine using Neon DB
- Use `asyncpg` driver
- Implement `AsyncSessionLocal`

### Task 2.2 – DB Session Dependency
- Implement async `get_db_session()`
- Ensure session cleanup with `async with`

---

## 🧩 TASK GROUP 3: Data Models
**Skills:** sqlmodel-task-models

### Task 3.1 – User Model
- Create `User` SQLModel
- Fields:
  - id (UUID, PK)
  - username (unique)
  - email (unique)
  - password_hash
  - created_at
- Relationship: `todos: List[Todo]`

### Task 3.2 – Todo Model
- Create `Todo` SQLModel
- Fields:
  - id (UUID, PK)
  - title (required)
  - description (optional)
  - completed (bool, default False)
  - owner_id (FK → User.id)
  - created_at
  - updated_at

---

## 🧩 TASK GROUP 4: JWT Authentication
**Skills:** fastapi-jwt, fastapi-jwt-auth

### Task 4.1 – JWT Utility Functions
- Create token creation function
- Token expiry = 7 days
- Algorithm = HS256

### Task 4.2 – Password Security
- Implement password hashing (bcrypt)
- Implement password verification

### Task 4.3 – Auth Routes
- POST `/auth/register`
  - Validate input
  - Hash password
  - Save user
  - Return JWT
- POST `/auth/login`
  - Verify credentials
  - Return JWT
- GET `/auth/me`
  - Decode JWT
  - Return user

---

## 🧩 TASK GROUP 5: Auth Dependencies
**Skills:** fastapi-jwt-auth

### Task 5.1 – Current User Dependency
- Extract JWT from Authorization header
- Decode token
- Fetch user from DB
- Raise 401 if invalid/expired

---

## 🧩 TASK GROUP 6: Secure Todo CRUD
**Skills:** secure-task-crud

### Task 6.1 – Create Todo
- POST `/todos/`
- Require JWT
- Assign owner_id from token

### Task 6.2 – Get All Todos
- GET `/todos/`
- Return only current user todos

### Task 6.3 – Get Single Todo
- GET `/todos/{id}`
- Validate ownership
- Return 404 if not found

### Task 6.4 – Update Todo
- PUT `/todos/{id}`
- Allow partial updates
- Validate ownership

### Task 6.5 – Delete Todo
- DELETE `/todos/{id}`
- Validate ownership
- Hard delete

---

## 🧩 TASK GROUP 7: API Assembly
**Skills:** fastapi-jwt-auth, sqlmodel-db

### Task 7.1 – Route Registration
- Register auth routes
- Register todo routes
- Apply dependencies globally where needed

### Task 7.2 – Application Entry Point
- Create `main.py`
- Initialize FastAPI app
- Include routers
- Enable CORS

---

## 🧩 TASK GROUP 8: Validation & Error Handling
**Skills:** secure-task-crud

### Task 8.1 – Error Responses
- 401 Unauthorized → Invalid JWT
- 403 Forbidden → Ownership violation
- 404 Not Found → Missing resource
- 422 Validation error

---

## 🧩 TASK GROUP 9: Final Verification
**Skills:** ALL

### Task 9.1 – Backend Startup
- Run using:
  `uv run uvicorn app.main:app --reload`

### Task 9.2 – API Validation
- Test JWT via Swagger
- Test all CRUD routes
- Confirm user isolation

---

## ✅ FINAL EXPECTATION

- Fully working FastAPI backend
- UV-managed environment
- Async Neon PostgreSQL
- JWT auth with 7-day expiry
- Secure, user-isolated Todo CRUD
- Modular, production-ready code
- No manual fixes required

Generate implementation strictly following this task file.
All listed skills MUST be applied in real code.
```

## Response snapshot

Created comprehensive task breakdown for the FastAPI Todo Application Backend implementation. Generated atomic, ordered, and directly executable tasks organized by user story following the checklist format. All mandatory skills were incorporated (uv-initialization, sqlmodel-task-models, fastapi-jwt-auth, neon-async-db, secure-task-crud, sqlmodel-db, fastapi-jwt) across 7 phases: Project Setup, Foundational Components, Authentication System, Secure Todo CRUD, API Assembly, Error Handling, and Final Verification.

## Outcome

- ✅ Impact: Complete task breakdown with all required skills applied across 38 atomic tasks
- 🧪 Tests: No tests created as this is a task breakdown document
- 📁 Files: Created specs/001-fastapi-todo-backend/tasks.md with comprehensive task list
- 🔁 Next prompts: Proceed to implementation with /sp.implement to execute tasks
- 🧠 Reflection: Tasks organized by user story enabling independent implementation and testing

## Evaluation notes (flywheel)

- Failure modes observed: None - successful task breakdown completion
- Graders run and results (PASS/FAIL): N/A for task generation
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation with /sp.implement