from sqlmodel import select, update, delete
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from uuid import UUID

from .models import Todo, User
from .database import get_async_session
from sqlmodel.ext.asyncio.session import AsyncSession


async def create_todo(session: AsyncSession, title: str, description: Optional[str], owner_id: UUID) -> Todo:
    """
    Create a new todo for the given owner.

    Args:
        session: Database session
        title: Title of the todo (1-100 characters)
        description: Optional description of the todo
        owner_id: UUID of the user who owns this todo

    Returns:
        The created Todo object
    """
    todo = Todo(
        title=title,
        description=description,
        owner_id=owner_id
    )

    session.add(todo)
    await session.commit()
    await session.refresh(todo)

    return todo


async def get_todos_by_owner(session: AsyncSession, owner_id: UUID) -> List[Todo]:
    """
    Get all todos for a specific owner.

    Args:
        session: Database session
        owner_id: UUID of the user whose todos to retrieve

    Returns:
        List of Todo objects belonging to the owner
    """
    statement = select(Todo).where(Todo.owner_id == owner_id)
    result = await session.exec(statement)
    return result.all()


async def get_todo_by_id(session: AsyncSession, todo_id: UUID, owner_id: UUID) -> Optional[Todo]:
    """
    Get a specific todo by ID for a specific owner (enforcing ownership).

    Args:
        session: Database session
        todo_id: UUID of the todo to retrieve
        owner_id: UUID of the user who should own this todo

    Returns:
        Todo object if it exists and belongs to the owner, None otherwise
    """
    statement = select(Todo).where(Todo.id == todo_id, Todo.owner_id == owner_id)
    result = await session.exec(statement)
    return result.first()


async def update_todo(session: AsyncSession, todo_id: UUID, owner_id: UUID,
                     title: Optional[str] = None, description: Optional[str] = None,
                     completed: Optional[bool] = None) -> Optional[Todo]:
    """
    Update a specific todo for a specific owner (enforcing ownership).

    Args:
        session: Database session
        todo_id: UUID of the todo to update
        owner_id: UUID of the user who should own this todo
        title: New title (optional)
        description: New description (optional)
        completed: New completed status (optional)

    Returns:
        Updated Todo object if successful and belongs to the owner, None otherwise
    """
    # First, verify ownership by getting the todo
    todo = await get_todo_by_id(session, todo_id, owner_id)
    if not todo:
        return None

    # Prepare update data
    update_data = {}
    if title is not None:
        update_data["title"] = title
    if description is not None:
        update_data["description"] = description
    if completed is not None:
        update_data["completed"] = completed

    if update_data:  # Only update if there's data to update
        statement = (
            update(Todo)
            .where(Todo.id == todo_id, Todo.owner_id == owner_id)
            .values(**update_data)
        )

        await session.exec(statement)
        await session.commit()

        # Refresh the todo to get the updated values
        await session.refresh(todo)

    return todo


async def delete_todo(session: AsyncSession, todo_id: UUID, owner_id: UUID) -> bool:
    """
    Delete a specific todo for a specific owner (enforcing ownership).

    Args:
        session: Database session
        todo_id: UUID of the todo to delete
        owner_id: UUID of the user who should own this todo

    Returns:
        True if deletion was successful, False if todo didn't exist or wasn't owned by user
    """
    statement = (
        delete(Todo)
        .where(Todo.id == todo_id, Todo.owner_id == owner_id)
    )

    result = await session.exec(statement)
    await session.commit()

    # If rowcount > 0, then at least one row was deleted
    return result.rowcount > 0