# Data Model: FastAPI Todo Application Backend

## Entity Definitions

### User Entity
**Fields**:
- id (UUID, Primary Key) - Unique identifier for each user
- username (str, unique, indexed) - Unique username for the user account
- email (str, unique, indexed) - Unique email address for the user
- password_hash (str) - BCrypt hash of the user's password
- created_at (datetime, default now) - Timestamp when user was created
- updated_at (datetime, default now, onupdate now) - Timestamp when user was last updated

**Relationships**:
- todos: One-to-many relationship with Todo entity (cascade delete)

**Validation Rules**:
- Username: 3-50 characters, alphanumeric with underscores/hyphens allowed
- Email: Valid email format
- Username and email must be unique across all users

### Todo Entity
**Fields**:
- id (UUID, Primary Key) - Unique identifier for each todo item
- title (str, 1-100 characters) - Title of the todo item
- description (str, optional, max 1000 chars) - Optional description of the todo
- completed (bool, default False) - Whether the todo is completed or not
- owner_id (UUID, Foreign Key → User.id) - Reference to the user who owns this todo
- created_at (datetime, default now) - Timestamp when todo was created
- updated_at (datetime, default now, onupdate now) - Timestamp when todo was last updated

**Relationships**:
- owner: Many-to-one relationship with User entity (todo belongs to one user)

**Validation Rules**:
- Title: Required, 1-100 characters
- Description: Optional, max 1000 characters
- Owner_id: Must reference an existing user
- Only the owner can access/modify this todo

## State Transitions

### Todo State Transitions
- `created` → `active`: When a new todo is created (initial state)
- `active` → `completed`: When the completed field is set to True
- `completed` → `active`: When the completed field is set to False
- `any_state` → `deleted`: When the todo is deleted

### User State Transitions
- `registered` → `active`: When user successfully completes registration
- `active` → `suspended`: When account is temporarily disabled (not currently implemented)

## Database Schema Constraints

### Indexes
- User: Index on username and email fields for fast lookups
- Todo: Index on owner_id for efficient ownership queries
- Todo: Composite index on (owner_id, completed) for common query patterns

### Foreign Key Constraints
- Todo.owner_id references User.id with CASCADE delete
- Prevents orphaned todos when users are deleted

### Check Constraints
- Todo.title length between 1-100 characters
- User.username length between 3-50 characters

## API Contract Implications

### Request Validation
- User registration: Validate email format, password strength, username validity
- Todo creation: Validate title length and required fields
- Todo updates: Allow partial updates with proper validation

### Response Formats
- User responses: Never include password_hash field
- Todo responses: Include owner information in a minimal format
- Error responses: Standardized format with {error: {message, code, details}}

## Security Considerations

### Data Isolation
- All queries filter by owner_id to prevent unauthorized access
- Authentication layer verifies JWT before database access
- Foreign key constraints prevent data inconsistency

### Audit Trail
- created_at and updated_at timestamps on all entities
- Future extension: Could add user_id to track who made changes