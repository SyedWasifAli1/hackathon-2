---
id: 0001
title: create-todo-frontend-spec
stage: spec
date: 2026-02-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-todo-frontend
branch: 001-todo-frontend
user: wasif
command: /sp.specify
labels: ["spec", "frontend", "todo-app", "authentication", "jwt"]
links:
  spec: ../specs/001-todo-frontend/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-todo-frontend/spec.md
 - specs/001-todo-frontend/checklists/requirements.md
tests:
 - none
---

## Prompt

Full-Stack Todo Application (Frontend)
1. Overview

Build a modern, production-grade frontend for a Todo Application using Next.js 16+ (App Router).
The frontend must integrate with an existing FastAPI + JWT backend, support authentication, protected routes, CRUD operations, and a modern + subtle 3D UI experience.

2. Tech Stack

Framework: Next.js 16+ (App Router)

Language: TypeScript

Styling: Tailwind CSS

3D / Motion UI:

Framer Motion (animations)

CSS 3D transforms (cards, hover depth)

Optional: Three.js / @react-three/fiber (light usage only)

HTTP Client: Axios

State Management: React Context + Hooks

Auth: JWT (Bearer Token)

Storage: localStorage (access token)

Linting: ESLint (Next.js default)

3. Application Pages & Routes
Public Pages
Route    Description
/    Home (Landing Page – marketing + CTA)
/auth/login    Login page
/auth/register    Register page
/about    About the application
/contact    Contact page
Protected Pages (JWT Required)
Route    Description
/dashboard    User dashboard
/dashboard/todos    Todo CRUD page
/dashboard/profile    Logged-in user profile
4. Routing & Protection Rules

Any route under /dashboard/* must be protected

If JWT token is missing or invalid:

Redirect user to /auth/login

Authentication check happens:

On client using AuthContext

On route using ProtectedRoute wrapper

5. Folder Structure (Next.js 16+ App Router)
frontend/
├─ app/
│  ├─ layout.tsx              # Root layout
│  ├─ page.tsx                # Home page
│  ├─ about/
│  │  └─ page.tsx
│  ├─ contact/
│  │  └─ page.tsx
│  ├─ auth/
│  │  ├─ login/
│  │  │  └─ page.tsx
│  │  └─ register/
│  │     └─ page.tsx
│  ├─ dashboard/
│  │  ├─ layout.tsx           # Dashboard layout (protected)
│  │  ├─ page.tsx             # Dashboard home
│  │  ├─ todos/
│  │  │  └─ page.tsx
│  │  └─ profile/
│  │     └─ page.tsx
│
├─ components/
│  ├─ ui/
│  │  ├─ Button.tsx
│  │  ├─ Input.tsx
│  │  ├─ Card3D.tsx           # 3D hover card
│  │  └─ Loader.tsx
│  ├─ layout/
│  │  ├─ Navbar.tsx
│  │  ├─ Footer.tsx
│  │  └─ Sidebar.tsx
│  ├─ auth/
│  │  └─ ProtectedRoute.tsx
│  └─ todos/
│     ├─ TodoForm.tsx
│     ├─ TodoItem.tsx
│     └─ TodoList.tsx
│
├─ context/
│  └─ AuthContext.tsx
│
├─ services/
│  ├─ api.ts                  # Axios instance
│  ├─ auth.service.ts
│  └─ todo.service.ts
│
├─ hooks/
│  ├─ useAuth.ts
│  └─ useTodos.ts
│
├─ styles/
│  └─ globals.css
│
├─ middleware.ts              # Route protection (optional)
├─ tailwind.config.ts
├─ tsconfig.json
└─ package.json
6. Authentication Flow
Login / Register

User submits login or register form

Frontend calls:

POST /auth/login

POST /auth/register

Backend returns:

{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}

Store token in localStorage

Update AuthContext

Redirect to /dashboard

Logout

Clear token from localStorage

Reset auth state

Redirect to /auth/login

7. API Integration
Axios Configuration

Base URL: http://localhost:8000

Automatically attach JWT token:

Authorization: Bearer <token>
API Services
Auth

login(email, password)

register(username, email, password)

getMe()

Todos

getTodos()

createTodo(data)

updateTodo(id, data)

deleteTodo(id)

8. Todo UI & CRUD Behavior
Todo Fields

title

description (optional)

completed (boolean)

UI Behavior

Add Todo → Modal / Card form

List Todos → Animated list

Toggle Complete → Checkbox + animation

Delete Todo → Confirm + animation

Real-time UI updates after API success

9. 3D & Modern UI Requirements
Visual Style

Glassmorphism cards

Soft shadows

Dark + Light mode ready

Gradient backgrounds

3D Effects

Todo cards tilt on hover (CSS transform: perspective)

Dashboard cards with depth

Buttons with micro-interactions

Framer Motion:

Page transitions

List animations

Hover scale & fade

⚠️ 3D effects must be lightweight (no heavy scenes)

10. State Management

AuthContext

user

token

login()

logout()

Todos Hook

todos[]

loading

create / update / delete handlers

11. Error & Loading Handling

Global loading indicator

API error handling:

401 → auto logout

Validation errors → show messages

Empty states for todos

12. Security Rules

Never expose JWT in UI

Use HTTPS-ready structure

Protect dashboard routes

No API calls without token

13. Acceptance Criteria

Next.js 16+ App Router used

Component-based clean structure

Fully protected dashboard

JWT auth fully working

Todo CRUD fully functional

Modern + 3D UI implemented

Clean, readable, scalable code

14. Goal

Deliver a portfolio-grade frontend that looks modern, feels smooth, and integrates perfectly with a FastAPI JWT backend.

## Response snapshot

Created comprehensive specification for the Full-Stack Todo Application frontend, including user scenarios, functional requirements, key entities, and success criteria.

## Outcome

- ✅ Impact: Created complete feature specification for todo application frontend with authentication, CRUD operations, and 3D UI elements
- 🧪 Tests: none
- 📁 Files: specs/001-todo-frontend/spec.md, specs/001-todo-frontend/checklists/requirements.md
- 🔁 Next prompts: /sp.plan to create implementation plan, /sp.tasks to generate development tasks
- 🧠 Reflection: Comprehensive spec with clear user stories and testable requirements enables efficient implementation planning

## Evaluation notes (flywheel)

- Failure modes observed: None; successful specification creation with proper branching and file organization
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
