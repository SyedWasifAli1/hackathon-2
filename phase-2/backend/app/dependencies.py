import uuid
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError
from .auth import decode_access_token, get_user_by_id
from .database import get_async_session
from .models import User
from typing import AsyncGenerator

security = HTTPBearer()

async def get_current_user(
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
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(credentials.credentials)
        user_id: str = payload.get("sub")

        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await get_user_by_id(user_id, session)
    if user is None:
        raise credentials_exception

    return user