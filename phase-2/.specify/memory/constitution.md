<!-- SYNC IMPACT REPORT:
Version change: 1.0.0 -> 1.1.0
Added sections: Backend Business Logic, Frontend Business Logic, Security & Permissions Framework
Removed sections: None
Modified principles: None (added business logic sections)
Templates requiring updates: ✅ updated - .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: None
-->
# Hackathon Todo Application Constitution

## Version
**Version**: 1.1.0 | **Ratified**: 2026-02-05 | **Last Amended**: 2026-02-05

## Overview
This constitution serves as the unbreakable governing principles and development guidelines for the hackathon full-stack Todo web application. It guides every specification, plan, task breakdown, and implementation decision made by Claude Code. Any deviation must be explicitly justified and updated in constitution.md only after approval.

## Core Principles

### 1. Spec-Driven Development (SDD) Purity
Every feature starts with clear, detailed specifications in /specs/. Always reference relevant specs with @specs/... notation. Update specs if requirements change — never bypass specs. Treat specifications, architecture history, prompt history, tests, and auto-evaluations as first-class artifacts.

### 2. Code Quality & Maintainability
Write clean, readable, modular code following best practices. Use TypeScript fully in frontend (strict types, no 'any'). Use Pydantic/SQLModel models for validation in backend. Follow naming conventions: camelCase for JS/TS, snake_case for Python variables. Keep functions small, single-responsibility. No magic numbers/strings — use constants. Comment complex logic, but prefer self-documenting code.

### 3. Testing Standards
Write unit/integration tests for every core piece of logic (e.g., task creation/validation, JWT verification, API endpoints). Aim for high coverage on business logic and auth flows. Use pytest for backend, Jest + React Testing Library for frontend (where applicable). Tests must be part of implementation tasks.

### 4. Security & User Isolation (Critical)
Enforce strict ownership: Every task operation MUST check user_id from JWT matches URL's user_id. Use shared BETTER_AUTH_SECRET env var for JWT signing/verification. Never expose other users' data. Handle 401 Unauthorized properly on invalid/missing token. Validate all inputs (title length 1-200 chars, description max 1000). Use HTTPS in production mindset (CORS configured properly).

### 5. Performance & Scalability
Optimize database queries (use indexes on user_id, completed). Prefer server components in Next.js; minimize client-side JS. Avoid unnecessary re-renders (use memo, useCallback where needed). Keep API responses lightweight (no over-fetching). Design for Neon Serverless (connection pooling if needed).

### 6. User Experience & UI Consistency
Responsive design with Tailwind CSS (mobile-first). Intuitive task list: show title, status, dates; color-code completed/pending. Clear feedback on actions (toasts for success/error). Protected routes: redirect to login if not authenticated. Follow modern UX patterns (e.g., optimistic updates if possible).

### 7. Architecture & Technical Governance
Monorepo with clear separation: frontend/, backend/, specs/. Use docker-compose.yml for local dev (frontend + backend together). Env vars for secrets (DATABASE_URL, BETTER_AUTH_SECRET, etc.). JWT stateless auth — no sessions in backend. Error handling: Proper HTTPException in FastAPI, meaningful frontend errors. Follow existing CLAUDE.md guidelines in root/frontend/backend.

### 8. AI Collaboration & Workflow
Always read Root CLAUDE.md, relevant feature spec, API spec, database schema before any action. Iterate transparently: if unclear, ask for clarification via /sp.clarify. Commit changes meaningfully after each /sp.implement. Preserve reusable intelligence: update specs/architecture docs after changes.

## Development Workflow & Standards

The project follows a strict Spec-Kit Plus workflow where NO manual coding is allowed — all code changes must be made via /sp.implement after specs, plans, and tasks are properly defined. The tech stack is fixed: Next.js 16+ (TypeScript, Tailwind CSS, App Router, server components preferred), FastAPI (Python), SQLModel ORM, Neon Serverless PostgreSQL, Better Auth with JWT for authentication.

All API endpoints follow a RESTful pattern under /api/{user_id}/tasks with JWT Bearer token required in every request. Core features include User signup/signin, Task CRUD (create/read/update/delete/toggle complete), and user-specific data isolation (only see/modify own tasks).

The development process must follow these slash commands: /sp.specify, /sp.clarify, /sp.plan, /sp.tasks, /sp.implement. This ensures a disciplined approach to software development with clear separation between specification, planning, and implementation phases.

## Project Structure

The monorepo structure includes:
- `/frontend`: Next.js 16+ application (TypeScript, Tailwind CSS, App Router)
- `/backend`: FastAPI server (Python, SQLModel ORM)
- `/specs`: Organized specifications (features/api/database/ui)
- `/.specify`: Configuration and templates for the Spec-Kit Plus workflow
- `/history`: Historical records (prompts, ADRs)

## Technology Stack Constraints

- Frontend: Next.js 16+, TypeScript, Tailwind CSS, App Router (server components preferred)
- Backend: FastAPI, Python, SQLModel ORM, Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT tokens
- Development: Strict spec-driven approach using Spec-Kit Plus commands
- Database: SQLModel schemas with Neon Serverless PostgreSQL
- Styling: Mobile-first responsive design with Tailwind CSS

## Compliance & Quality Gates

All development must adhere to the following non-negotiable requirements:
- Every implementation must be preceded by proper specifications in /specs/
- Code changes must be traced back to specific tasks from /sp.tasks
- All code must pass through /sp.implement process (no direct manual coding)
- Security requirements must be validated before merging
- All tests must pass before code is accepted
- Code reviews must verify compliance with all constitution principles
- Architecture decisions must follow the documented patterns
- Data isolation requirements must be strictly enforced

## Governance & Amendment Process

This constitution may only be amended through explicit approval and a formal update process:
1. Any proposed amendment must be documented with clear rationale
2. Amendment must be reviewed and approved by project stakeholders
3. Version number must be incremented according to semantic versioning
4. All dependent templates and configurations must be updated
5. Sync impact report must be maintained showing affected artifacts

Amendment types:
- MAJOR: Backward incompatible governance/principle removals or redefinitions
- MINOR: New principle/section added or materially expanded guidance
- PATCH: Clarifications, wording, typo fixes, non-semantic refinements

## Backend Business Logic

The backend follows a FastAPI architecture with JWT authentication and PostgreSQL/Neon database integration. The business logic encompasses:

### Authentication System (auth.py)
- **User Registration:**
  - Input validation: email format, password minimum 6 characters, username uniqueness
  - Password hashing using Passlib
  - JWT token generation with 7-day expiry
  - Secure user creation in database
- **User Login:**
  - Credential validation against hashed passwords
  - JWT token generation upon successful authentication
  - Secure session management
- **Current User Resolution:**
  - JWT token extraction from Authorization header
  - Token validation and decoding
  - User object resolution for protected endpoints
- **Permission Enforcement:**
  - All `/api/*` routes require valid JWT tokens
  - Automatic user identification from token claims

### Todo CRUD Operations (crud.py)
- **Create Todo:**
  - Input validation: title required, description optional
  - Automatic assignment of `owner_id` from current user
  - Database persistence with proper error handling
- **Read Todos:**
  - Fetch only todos where `owner_id == current_user_id`
  - Return filtered results to prevent cross-user data access
- **Read Single Todo:**
  - ID-based lookup with ownership verification
  - Return 404 if not found or 401 if not owned by user
- **Update Todo:**
  - Ownership verification before modification
  - Field validation for provided parameters
  - Safe update operations with proper error handling
- **Delete Todo:**
  - Ownership verification before deletion
  - Return success confirmation upon successful deletion

### Database Layer
- One-to-many relationship: User → Todos
- SQLAlchemy ORM with proper foreign key constraints
- Dependency injection for database sessions in all endpoints
- Comprehensive exception handling (404, 401, 400 errors)

## Frontend Business Logic

The frontend follows a Next.js architecture with TypeScript and component-based design. The business logic encompasses:

### Authentication Management (AuthContext)
- **Login Flow:**
  - Form submission to `/api/auth/login`
  - JWT token storage in browser's localStorage
  - AuthContext state updates
  - Redirect to `/dashboard` upon successful login
- **Registration Flow:**
  - Form submission to `/api/auth/register`
  - JWT token storage in browser's localStorage
  - AuthContext initialization
  - Redirect to `/dashboard` after account creation
- **Logout Flow:**
  - Token removal from localStorage
  - AuthContext cleanup
  - Redirect to homepage

### Protected Route System (ProtectedRoute.tsx)
- JWT token validation from AuthContext or localStorage
- Automatic redirect to login page if token is invalid or expired
- Allow access only for authenticated users

### Todo Management Operations
- **Fetch Todos:**
  - On `/todos` page load, call `GET /api/todos/`
  - State population with fetched todos
- **Create Todo:**
  - Open TodoForm component
  - Submit POST request to `/api/todos/`
  - Append new todo to local state
- **Update Todo:**
  - Edit via TodoForm or toggle completion status
  - Send PUT request to `/api/todos/{id}`
  - Update todo in local state
- **Delete Todo:**
  - Send DELETE request to `/api/todos/{id}`
  - Remove todo from local state

### State Management
- AuthContext handles user authentication state and JWT
- Component-local state for todo data management
- Axios instances configured with JWT headers for all API calls

### Form Validation
- Frontend validation for required fields, email formats, password length
- Validation patterns that match backend requirements
- User-friendly error messages and feedback

### UI Component Architecture
- **Navigation Bar:** Dynamic display of login/register (unauthenticated) vs logout/dashboard (authenticated)
- **Footer:** Static application information
- **TodoCard:** Display of title, description, and completion status toggle
- **TodoForm:** Creation and editing interface with validation

## Security & Permissions Framework

- JWT token required for all `/api/*` routes
- Strict user isolation: users can only access their own todos
- Passwords are never returned from API responses
- JWT tokens expire after 7 days
- Frontend automatically redirects unauthenticated users from protected routes
- Backend enforces ownership verification on all data access operations

## Accountability & Verification

The following accountability measures ensure adherence to this constitution:
- All code changes must be tracked through the PHR (Prompt History Record) system
- Architectural decisions must be documented in ADRs when significant
- Specifications must be validated before implementation
- Security requirements must be tested and verified
- Peer reviews must confirm constitutional compliance
- Automated checks should verify conformance where possible