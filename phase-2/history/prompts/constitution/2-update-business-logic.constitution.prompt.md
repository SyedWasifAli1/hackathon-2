---
id: 2
title: Update Business Logic in Constitution
stage: constitution
date: 2026-02-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: Claude
command: /sp.constitution
labels: [constitution, business-logic, backend, frontend, security]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
---

## Prompt

```
I want you to generate the **business logic** for a full-stack Todo application following the **SP.constitution standard**. The application includes **FastAPI backend** with **JWT authentication**, **PostgreSQL/Neon DB**, and **Next.js frontend** (TypeScript, component-based). The business logic should define **all functional flows, validations, permissions, and data handling rules** for backend and frontend.

---

### **Backend Business Logic (FastAPI + JWT + SQLAlchemy)**

1. **Authentication (auth.py)**
   - **Register:**
     - Input: `{ username, email, password }`
     - Validation: email format, password min 6 characters, username unique
     - Hash password using Passlib
     - Create user in DB
     - Return JWT token with 7-day expiry
   - **Login:**
     - Input: `{ email, password }`
     - Validation: check if email exists, verify password hash
     - Return JWT token with 7-day expiry
   - **Current User:**
     - Extract JWT from `Authorization` header
     - Decode and validate token
     - Return user object
   - **Permissions:** All `/todos` routes require valid JWT token

2. **Todos CRUD (crud.py)**
   - **Create Todo**
     - Input: `{ title, description }`
     - Validation: title required, description optional
     - Assign `owner_id` from current user
     - Save to DB
   - **Read Todos**
     - Fetch all todos where `owner_id == current user id`
     - Return list of todos
   - **Read Single Todo**
     - Fetch todo by ID
     - Verify `owner_id == current user id`
     - Return todo
     - Error if not owner or not found
   - **Update Todo**
     - Input: `{ title?, description?, completed? }`
     - Validate fields exist if provided
     - Verify ownership
     - Update DB and return updated todo
   - **Delete Todo**
     - Verify ownership
     - Delete from DB
     - Return success message

3. **Database Logic**
   - One-to-many relation: User → Todos
   - Use SQLAlchemy ORM models
   - Dependency injection for DB session in all endpoints
   - Handle exceptions: 404 (not found), 401 (unauthorized), 400 (validation errors)

---

### **Frontend Business Logic (Next.js + TypeScript + Axios + JWT)**

1. **Authentication (AuthContext + Login/Register)**
   - **Login**
     - Submit form → call `/auth/login`
     - Store JWT token in `localStorage`
     - Update AuthContext with user info
     - Redirect to `/dashboard`
   - **Register**
     - Submit form → call `/auth/register`
     - Store JWT token in `localStorage`
     - Update AuthContext
     - Redirect to `/dashboard`
   - **Logout**
     - Remove token from `localStorage`
     - Clear AuthContext
     - Redirect to `/`

2. **Protected Routes (ProtectedRoute.tsx)**
   - Check JWT token in AuthContext or localStorage
   - If invalid or expired → redirect to login
   - If valid → allow access

3. **Todos CRUD**
   - **Fetch Todos**
     - On `/todos` page load, call `GET /todos/`
     - Populate state with todos
   - **Create Todo**
     - Open `TodoForm`, submit → POST `/todos/`
     - Append new todo to state
   - **Update Todo**
     - Edit in `TodoForm` or toggle completed → PUT `/todos/{id}`
     - Update todo in state
   - **Delete Todo**
     - Call DELETE `/todos/{id}`
     - Remove todo from state

4. **State Management**
   - AuthContext manages user state and JWT
   - Todo state can be local state in `/todos` page
   - All API calls use Axios instance with JWT header

5. **Validation**
   - Frontend form validation: required fields, email format, min password length
   - Backend validation must match frontend

6. **UI Components**
   - **Navbar:** show login/register if unauthenticated, logout/dashboard links if authenticated
   - **Footer:** static info
   - **TodoCard:** display title, description, completed toggle
   - **TodoForm:** create/edit todo with validation

---

### **Security & Permissions**
- JWT required for all `/todos` routes
- Users can only access their own todos
- Passwords are never returned
- Token expires in 7 days
- Frontend redirects unauthenticated users from protected routes

---

### **Expected Output**
- Business logic flows for **all backend and frontend endpoints**
- Validations, permissions, and error handling
- Data flow from frontend → API → DB → frontend
- Clear modular structure:
  - Backend: auth.py, crud.py, models.py, main.py
  - Frontend: AuthContext, ProtectedRoute, Todos pages/components
- Ready to implement in SP.constitution spec-kit project

---

Generate **backend + frontend business logic** in clear steps, including **all rules, validations, user flows, and permissions**. Ensure **JWT, CRUD, and protected routes** behavior is fully defined.
```

## Response snapshot

Updated the project constitution to include comprehensive backend and frontend business logic sections. The update adds detailed descriptions of authentication flows, CRUD operations, database layer specifications, state management, validation rules, UI component architecture, and security permissions. The constitution now covers all functional flows, validations, permissions, and data handling rules for both backend (FastAPI + JWT + SQLAlchemy) and frontend (Next.js + TypeScript + Axios + JWT) as requested.

## Outcome

- ✅ Impact: Enhanced constitution with detailed backend and frontend business logic specifications
- 🧪 Tests: No tests created as this is a governance document update
- 📁 Files: Updated .specify/memory/constitution.md to version 1.1.0 with new business logic sections
- 🔁 Next prompts: Continue with specification development following enhanced constitution guidelines
- 🧠 Reflection: The updated constitution now provides complete business logic specifications for implementation teams

## Evaluation notes (flywheel)

- Failure modes observed: None - successful enhancement of governance document
- Graders run and results (PASS/FAIL): N/A for governance document update
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementing features following enhanced constitution