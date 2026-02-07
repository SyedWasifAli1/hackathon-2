# Todo Console Application Specification

## Overview
A command-line Todo application that stores tasks in memory only (no database, no files). All logic must live in ONE file: main.py

## Features
1. Add Task
   - Title (required)
   - Description (optional)
2. View Tasks
   - Show ID, title, description, status
   - Status indicators: [ ] Pending, [x] Completed
3. Update Task
   - Update title and/or description by ID
4. Delete Task
   - Delete task by ID
5. Mark Task Complete / Incomplete
   - Toggle status by ID

## Data Model
- In-memory list of tasks
- Each task must have:
  - id (auto-increment integer)
  - title (string)
  - description (string)
  - completed (boolean)

## Application Flow
- Show a menu in a loop:
  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
  6. Exit
- Handle invalid input gracefully
- Never crash on wrong input

## Quality Requirements
- Functions must be small and single-purpose
- Use clear function names
- Use type hints where useful
- Follow clean console UX
- Code should look like written by a professional Python developer