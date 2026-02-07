from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from typing import Optional, List
import uuid

from .models import Todo, User
from .crud import (
    create_todo, get_todos_by_owner, get_todo_by_id,
    update_todo, delete_todo
)
from .dependencies import get_current_user
from .database import get_async_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .exceptions import BadRequestException, NotFoundException

# Create router for todo endpoints
router = APIRouter(prefix="/todos", tags=["todos"])


class CreateTodoRequest(BaseModel):
    title: str
    description: Optional[str] = None


class UpdateTodoRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: Optional[str]
    completed: bool
    owner_id: uuid.UUID


class TodoListResponse(BaseModel):
    todos: List[TodoResponse]


@router.post("/", response_model=TodoResponse)
async def create_new_todo(
    todo_data: CreateTodoRequest,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """
    Create a new todo for the authenticated user.
    """
    # Validate title length (1-100 characters)
    if len(todo_data.title) < 1 or len(todo_data.title) > 100:
        raise BadRequestException(
            message="Title must be between 1 and 100 characters"
        )

    # Limit description length if provided
    if todo_data.description and len(todo_data.description) > 1000:
        raise BadRequestException(
            message="Description must not exceed 1000 characters"
        )

    new_todo = await create_todo(
        session=session,
        title=todo_data.title,
        description=todo_data.description,
        owner_id=current_user.id
    )

    return TodoResponse(
        id=new_todo.id,
        title=new_todo.title,
        description=new_todo.description,
        completed=new_todo.completed,
        owner_id=new_todo.owner_id
    )


@router.get("/", response_model=TodoListResponse)
async def get_user_todos(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """
    Get all todos for the authenticated user.
    """
    todos = await get_todos_by_owner(session=session, owner_id=current_user.id)

    todo_responses = [
        TodoResponse(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            completed=todo.completed,
            owner_id=todo.owner_id
        )
        for todo in todos
    ]

    return TodoListResponse(todos=todo_responses)


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_single_todo(
    todo_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """
    Get a specific todo by ID for the authenticated user.
    """
    todo = await get_todo_by_id(session=session, todo_id=todo_id, owner_id=current_user.id)

    if not todo:
        raise NotFoundException(
            message="Todo not found or does not belong to you"
        )

    return TodoResponse(
        id=todo.id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        owner_id=todo.owner_id
    )


@router.put("/{todo_id}", response_model=TodoResponse)
async def update_existing_todo(
    todo_id: uuid.UUID,
    update_data: UpdateTodoRequest,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """
    Update a specific todo by ID for the authenticated user.
    """
    # Validate title length if provided
    if update_data.title and (len(update_data.title) < 1 or len(update_data.title) > 100):
        raise BadRequestException(
            message="Title must be between 1 and 100 characters"
        )

    # Limit description length if provided
    if update_data.description and len(update_data.description) > 1000:
        raise BadRequestException(
            message="Description must not exceed 1000 characters"
        )

    updated_todo = await update_todo(
        session=session,
        todo_id=todo_id,
        owner_id=current_user.id,
        title=update_data.title,
        description=update_data.description,
        completed=update_data.completed
    )

    if not updated_todo:
        raise NotFoundException(
            message="Todo not found or does not belong to you"
        )

    return TodoResponse(
        id=updated_todo.id,
        title=updated_todo.title,
        description=updated_todo.description,
        completed=updated_todo.completed,
        owner_id=updated_todo.owner_id
    )


@router.delete("/{todo_id}")
async def delete_specific_todo(
    todo_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """
    Delete a specific todo by ID for the authenticated user.
    """
    success = await delete_todo(
        session=session,
        todo_id=todo_id,
        owner_id=current_user.id
    )

    if not success:
        raise NotFoundException(
            message="Todo not found or does not belong to you"
        )

    return {"message": "Todo deleted successfully"}