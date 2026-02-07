from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import uuid
from .models import Todo, User
from .database import get_async_session
from .auth import get_current_user_from_token
from sqlmodel import select

# Create router for todos endpoints
router = APIRouter(prefix="/todos", tags=["todos"])


class TodoCreateRequest(BaseModel):
    title: str
    description: Optional[str] = None


class TodoUpdateRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: Optional[str]
    completed: bool
    owner_id: uuid.UUID


@router.post("/", response_model=TodoResponse)
async def create_todo(
    todo_data: TodoCreateRequest,
    current_user: User = Depends(get_current_user_from_token),
    session=Depends(get_async_session)
):
    """Create a new todo for the current user."""
    # Create new todo with owner_id from current user
    todo = Todo(
        title=todo_data.title,
        description=todo_data.description,
        owner_id=current_user.id
    )

    session.add(todo)
    await session.commit()
    await session.refresh(todo)

    return TodoResponse(
        id=todo.id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        owner_id=todo.owner_id
    )


@router.get("/", response_model=List[TodoResponse])
async def get_todos(
    current_user: User = Depends(get_current_user_from_token),
    session=Depends(get_async_session)
):
    """Get all todos for the current user."""
    statement = select(Todo).where(Todo.owner_id == current_user.id)
    result = await session.exec(statement)
    todos = result.all()

    return [
        TodoResponse(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            completed=todo.completed,
            owner_id=todo.owner_id
        )
        for todo in todos
    ]


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo_by_id(
    todo_id: uuid.UUID,
    current_user: User = Depends(get_current_user_from_token),
    session=Depends(get_async_session)
):
    """Get a specific todo by ID, ensuring it belongs to the current user."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)
    result = await session.exec(statement)
    todo = result.first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or you don't have permission to access it"
        )

    return TodoResponse(
        id=todo.id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        owner_id=todo.owner_id
    )


@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: uuid.UUID,
    todo_data: TodoUpdateRequest,
    current_user: User = Depends(get_current_user_from_token),
    session=Depends(get_async_session)
):
    """Update a specific todo, ensuring it belongs to the current user."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)
    result = await session.exec(statement)
    todo = result.first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or you don't have permission to access it"
        )

    # Update fields if provided
    if todo_data.title is not None:
        todo.title = todo_data.title
    if todo_data.description is not None:
        todo.description = todo_data.description
    if todo_data.completed is not None:
        todo.completed = todo_data.completed

    await session.commit()
    await session.refresh(todo)

    return TodoResponse(
        id=todo.id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        owner_id=todo.owner_id
    )


@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: uuid.UUID,
    current_user: User = Depends(get_current_user_from_token),
    session=Depends(get_async_session)
):
    """Delete a specific todo, ensuring it belongs to the current user."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)
    result = await session.exec(statement)
    todo = result.first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or you don't have permission to access it"
        )

    await session.delete(todo)
    await session.commit()

    return {"message": "Todo deleted successfully"}