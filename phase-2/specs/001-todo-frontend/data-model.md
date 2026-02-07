# Data Model: Full-Stack Todo Application (Frontend)

## Overview
Data model for the frontend components that interact with the backend API. This represents the client-side state and API contracts for the todo application.

## Entity: Todo
**Description**: Represents individual tasks managed by users

**Fields**:
- `id`: string (UUID) - Unique identifier for the todo
- `title`: string (max 100 characters) - Title of the task
- `description`: string (optional, max 500 characters) - Detailed description of the task
- `completed`: boolean - Completion status of the task
- `createdAt`: Date - Timestamp when todo was created
- `updatedAt`: Date - Timestamp when todo was last updated
- `userId`: string - Reference to the user who owns this todo

**Relationships**:
- Belongs to one `User` (via userId)

**Validation rules**:
- Title must be 1-100 characters
- Description can be 0-500 characters
- Completed defaults to false
- createdAt and updatedAt are automatically managed by backend

## Entity: User
**Description**: Represents authenticated users in the application

**Fields**:
- `id`: string (UUID) - Unique identifier for the user
- `username`: string - Username for the account
- `email`: string - Email address for the account
- `token`: string (client-side only) - JWT token for authentication
- `isLoggedIn`: boolean (client-side only) - Authentication status

**Validation rules**:
- Username and email are required
- Email must follow standard email format
- Password must be minimum 8 characters with mixed case, numbers, and special characters

## Entity: TodoFilter
**Description**: Optional client-side filtering parameters

**Fields**:
- `completed`: boolean (optional) - Filter by completion status
- `searchTerm`: string (optional) - Filter by title/description text

## State Transitions

### Todo State Transitions:
1. **New Todo Creation**:
   - Initial state: `completed: false`
   - Action: User creates a new todo
   - Result: Todo saved with `completed: false`, timestamps set

2. **Toggle Completion**:
   - Initial state: `completed: false` or `completed: true`
   - Action: User toggles completion status
   - Result: `completed` property flips, `updatedAt` updated

3. **Todo Deletion**:
   - Initial state: Todo exists in the system
   - Action: User deletes the todo
   - Result: Todo removed from local state and backend

### Authentication State Transitions:
1. **Login Success**:
   - Initial state: Unauthenticated
   - Action: Successful login with valid credentials
   - Result: User becomes authenticated, token stored, redirect to dashboard

2. **Logout**:
   - Initial state: Authenticated
   - Action: User triggers logout
   - Result: Token cleared, user state reset, redirect to login

3. **Token Expiry**:
   - Initial state: Authenticated with valid token
   - Action: Token expires or becomes invalid
   - Result: User becomes unauthenticated, redirect to login