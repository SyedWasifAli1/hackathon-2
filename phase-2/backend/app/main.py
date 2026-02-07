from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .database import create_db_and_tables
from .auth import router as auth_router
from .todo_routes import router as todos_router
from .config import settings
from .exceptions import TodoException


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    await create_db_and_tables()
    yield
    # Cleanup on shutdown if needed


app = FastAPI(
    title="Todo Application API",
    description="Secure Todo application backend with JWT authentication",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # Additional security headers
    allow_origin_regex=".*",
)


@app.get("/")
async def root():
    return {"message": "Todo Application Backend API"}


# Include authentication routes
app.include_router(auth_router)

# Include todos routes
app.include_router(todos_router)


from fastapi.responses import JSONResponse

@app.exception_handler(TodoException)
async def todo_exception_handler(request, exc: TodoException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail
    )

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred", "error": str(exc)}
    )