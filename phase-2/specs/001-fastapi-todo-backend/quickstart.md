# Quickstart Guide: FastAPI Todo Application Backend

## Prerequisites

- Python 3.11+
- UV package manager installed
- Neon Serverless PostgreSQL database setup
- Environment with ability to run async Python applications

## Setup Instructions

### 1. Clone and Navigate to Backend Directory
```bash
cd backend
```

### 2. Initialize UV Project
```bash
uv init
```

### 3. Install Dependencies
```bash
uv add fastapi uvicorn sqlmodel asyncpg python-jose[cryptography] passlib[bcrypt] python-dotenv
```

### 4. Configure Environment Variables
Create a `.env` file with the following variables:
```env
DATABASE_URL=postgresql+asyncpg://username:password@host:port/dbname
JWT_SECRET=your-super-secret-jwt-key-change-this!
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080  # 7 days in minutes
REFRESH_TOKEN_EXPIRE_DAYS=30
```

### 5. Initialize Database Tables
Run the following to create database tables:
```bash
python -c "from app.database import create_db_and_tables; import asyncio; asyncio.run(create_db_and_tables())"
```

## Running the Application

### Development Mode
```bash
uv run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Production Mode
```bash
uv run uvicorn app.main:app --workers 4
```

## API Endpoints

### Authentication
- `POST /auth/register` - Create new user account
- `POST /auth/login` - Authenticate and get JWT token
- `GET /auth/me` - Get current user information

### Todo Management
- `POST /todos/` - Create a new todo
- `GET /todos/` - Get all todos for current user
- `GET /todos/{id}` - Get a specific todo
- `PUT /tos/{id}` - Update a specific todo
- `DELETE /todos/{id}` - Delete a specific todo

## Testing the API

### Register a New User
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "SecurePass123!"
  }'
```

### Login to Get Token
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePass123!"
  }'
```

### Create a Todo (with JWT token)
```bash
curl -X POST http://localhost:8000/todos/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE" \
  -d '{
    "title": "Sample Todo",
    "description": "This is a sample todo item"
  }'
```

## Configuration Details

### JWT Settings
- Algorithm: HS256
- Expiration: 7 days (configurable in .env)
- Secret key: Stored in JWT_SECRET environment variable

### Database Settings
- Engine: Async PostgreSQL (asyncpg driver)
- ORM: SQLModel
- Connection pooling: Handled automatically by asyncpg

### Security Features
- Passwords hashed with bcrypt (12 rounds)
- JWT token validation on all protected routes
- User isolation - users can only access their own todos
- Input validation using Pydantic models