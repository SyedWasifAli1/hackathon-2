---
id: 1
title: Create Hackathon App Constitution
stage: constitution
date: 2026-02-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: Claude
command: /sp.constitution
labels: [constitution, spec-driven-development, governance]
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
/sp.constitution

Create a comprehensive project constitution for a hackathon full-stack Todo web application (Phase 2). This constitution will serve as the unbreakable governing principles and development guidelines for the entire project. It must guide every specification, plan, task breakdown, and implementation decision made by Claude Code.

Project Context:
- This is a multi-user Todo app evolved from a console version.
- Monorepo structure: hackathon-todo/ with /frontend (Next.js 16+ App Router), /backend (FastAPI + SQLModel), /specs (organized by features/api/database/ui), /.spec-kit/config.yaml, multiple CLAUDE.md files (root, frontend, backend).
- Tech stack fixed: Next.js 16+ (TypeScript, Tailwind CSS, App Router, server components preferred), FastAPI (Python), SQLModel ORM, Neon Serverless PostgreSQL, Better Auth with JWT for authentication.
- Core features: User signup/signin, Task CRUD (create/read/update/delete/toggle complete), user-specific data isolation (only see/modify own tasks).
- API: RESTful endpoints under /api/{user_id}/tasks with JWT Bearer token required in every request.
- Development rules: Strictly spec-driven using Spec-Kit Plus workflow. NO manual coding allowed — all code changes via /sp.implement after specs, plans, and tasks. Use slash commands: /sp.specify, /sp.clarify, /sp.plan, /sp.tasks, /sp.implement.

Core Principles (must enforce these in every decision):

1. Spec-Driven Development (SDD) Purity
   - Every feature starts with clear, detailed specifications in /specs/.
   - Always reference relevant specs with @specs/... notation.
   - Update specs if requirements change — never bypass specs.
   - Treat specifications, architecture history, prompt history, tests, and auto-evaluations as first-class artifacts.

2. Code Quality & Maintainability
   - Write clean, readable, modular code following best practices.
   - Use TypeScript fully in frontend (strict types, no 'any').
   - Use Pydantic/SQLModel models for validation in backend.
   - Follow naming conventions: camelCase for JS/TS, snake_case for Python variables.
   - Keep functions small, single-responsibility.
   - No magic numbers/strings — use constants.
   - Comment complex logic, but prefer self-documenting code.

3. Testing Standards
   - Write unit/integration tests for every core piece of logic (e.g., task creation/validation, JWT verification, API endpoints).
   - Aim for high coverage on business logic and auth flows.
   - Use pytest for backend, Jest + React Testing Library for frontend (where applicable).
   - Tests must be part of implementation tasks.

4. Security & User Isolation (Critical)
   - Enforce strict ownership: Every task operation MUST check user_id from JWT matches URL's user_id.
   - Use shared BETTER_AUTH_SECRET env var for JWT signing/verification.
   - Never expose other users' data.
   - Handle 401 Unauthorized properly on invalid/missing token.
   - Validate all inputs (title length 1-200 chars, description max 1000).
   - Use HTTPS in production mindset (CORS configured properly).

5. Performance & Scalability
   - Optimize database queries (use indexes on user_id, completed).
   - Prefer server components in Next.js; minimize client-side JS.
   - Avoid unnecessary re-renders (use memo, useCallback where needed).
   - Keep API responses lightweight (no over-fetching).
   - Design for Neon Serverless (connection pooling if needed).

6. User Experience & UI Consistency
   - Responsive design with Tailwind CSS (mobile-first).
   - Intuitive task list: show title, status, dates; color-code completed/pending.
   - Clear feedback on actions (toasts for success/error).
   - Protected routes: redirect to login if not authenticated.
   - Follow modern UX patterns (e.g., optimistic updates if possible).

7. Architecture & Technical Governance
   - Monorepo with clear separation: frontend/, backend/, specs/.
   - Use docker-compose.yml for local dev (frontend + backend together).
   - Env vars for secrets (DATABASE_URL, BETTER_AUTH_SECRET, etc.).
   - JWT stateless auth — no sessions in backend.
   - Error handling: Proper HTTPException in FastAPI, meaningful frontend errors.
   - Follow existing CLAUDE.md guidelines in root/frontend/backend.

8. AI Collaboration & Workflow
   - Always read Root CLAUDE.md, relevant feature spec, API spec, database schema before any action.
   - Iterate transparently: if unclear, ask for clarification via /sp.clarify.
   - Commit changes meaningfully after each /sp.implement.
   - Preserve reusable intelligence: update specs/architecture docs after changes.

This constitution is the DNA of the project. Reference it in every phase. Any deviation must be explicitly justified and updated in constitution.md only after approval. Enforce these rules strictly for high-quality, secure, maintainable output.

Generate and save this as .specify/memory/constitution.md
```

## Response snapshot

Created a comprehensive project constitution for the hackathon Todo application with 8 core principles, governance structure, and compliance requirements. The constitution defines the unbreakable governing principles and development guidelines that will guide every specification, plan, task breakdown, and implementation decision. It enforces spec-driven development purity, code quality standards, security requirements, and proper development workflow using the Spec-Kit Plus commands.

## Outcome

- ✅ Impact: Created foundational governance document with 8 core principles covering SDD, code quality, testing, security, performance, UX, architecture, and AI collaboration
- 🧪 Tests: No tests created as this is a governance document
- 📁 Files: Created/updated .specify/memory/constitution.md with comprehensive constitution document
- 🔁 Next prompts: Implementation of features will follow spec-driven workflow (/sp.specify, /sp.plan, /sp.tasks, /sp.implement)
- 🧠 Reflection: The constitution establishes strong governance for the project, ensuring consistent development practices and quality standards across the team

## Evaluation notes (flywheel)

- Failure modes observed: None - successful creation of governance document
- Graders run and results (PASS/FAIL): N/A for governance document creation
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementing features following the established constitution