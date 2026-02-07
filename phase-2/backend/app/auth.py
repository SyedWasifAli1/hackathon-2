import uuid
from datetime import datetime, timedelta
from typing import Optional
from sqlmodel import select
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from contextlib import contextmanager
from fastapi import APIRouter
from pydantic import BaseModel
from .models import User
from .database import get_async_session
from .config import settings
from .exceptions import UnauthorizedException, BadRequestException

# Create router for auth endpoints
router = APIRouter(prefix="/auth", tags=["auth"])

# Password hashing context - using argon2 instead of bcrypt to avoid 72-byte password limit
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Security for JWT in authorization header
security = HTTPBearer()


class UserRegisterRequest(BaseModel):
    username: str
    email: str
    password: str


class UserLoginRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    email: str


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a plain password. Truncate to 72 bytes if needed to comply with bcrypt limits."""
    # Ensure password is no longer than 72 bytes for bcrypt
    if len(password.encode('utf-8')) > 72:
        # Truncate to 72 bytes and decode back to string
        password = password.encode('utf-8')[:72].decode('utf-8', errors='ignore')
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create JWT access token with expiration."""
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)

    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret, algorithm=settings.jwt_algorithm)
    return encoded_jwt


def decode_access_token(token: str) -> dict:
    """Decode JWT access token and return payload."""
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_user_by_email(email: str, session) -> Optional[User]:
    """Get user by email."""
    statement = select(User).where(User.email == email)
    result = await session.exec(statement)
    return result.first()


async def get_user_by_id(user_id: str, session) -> Optional[User]:
    """Get user by ID."""
    statement = select(User).where(User.id == uuid.UUID(user_id))
    result = await session.exec(statement)
    return result.first()


def create_access_token_for_user(user: User) -> str:
    """Create access token for a specific user."""
    data = {"sub": str(user.id)}
    return create_access_token(data)


async def authenticate_user(email: str, password: str, session) -> Optional[User]:
    """Authenticate user by email and password."""
    user = await get_user_by_email(email, session)
    if not user or not verify_password(password, user.password_hash):
        return None
    return user


def create_refresh_token(data: dict) -> str:
    """Create JWT refresh token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=30)  # 30 days expiry
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret, algorithm=settings.jwt_algorithm)
    return encoded_jwt


@router.post("/register", response_model=TokenResponse)
async def register_user(user_data: UserRegisterRequest, session=Depends(get_async_session)):
    """Register a new user and return JWT token."""
    # Check if user with email already exists
    existing_user = await get_user_by_email(user_data.email, session)
    if existing_user:
        raise BadRequestException(
            message="User with this email already exists"
        )

    # Hash password
    password_hash = get_password_hash(user_data.password)

    # Create new user
    user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=password_hash
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)

    # Create access token
    access_token = create_access_token_for_user(user)

    return {"access_token": access_token}


@router.post("/login", response_model=TokenResponse)
async def login_user(user_data: UserLoginRequest, session=Depends(get_async_session)):
    """Login user with email and password and return JWT token."""
    user = await authenticate_user(user_data.email, user_data.password, session)
    if not user:
        raise UnauthorizedException(
            message="Incorrect email or password"
        )

    access_token = create_access_token_for_user(user)

    return {"access_token": access_token}


async def get_current_user_from_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session=Depends(get_async_session)
) -> User:
    """
    Get current user from JWT token in Authorization header.

    Raises 401 Unauthorized if:
    - Token is missing
    - Token is invalid/expired
    - User doesn't exist in database
    """
    try:
        payload = decode_access_token(credentials.credentials)
        user_id: str = payload.get("sub")

        if user_id is None:
            raise UnauthorizedException(message="Could not validate credentials")
    except JWTError:
        raise UnauthorizedException(message="Could not validate credentials")

    user = await get_user_by_id(user_id, session)
    if user is None:
        raise UnauthorizedException(message="Could not validate credentials")

    return user


@router.get("/me", response_model=UserResponse)
async def get_current_user_data(current_user: User = Depends(get_current_user_from_token)):
    """Get current user's information."""
    return UserResponse(
        id=current_user.id,
        username=current_user.username,
        email=current_user.email
    )