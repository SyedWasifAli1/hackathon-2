# # app/mcp_server.py
# from uuid import UUID
# from typing import Optional, List
# from mcp.server.fastmcp import FastMCP
# from app import crud
# from app.database import get_async_session

# mcp = FastMCP(
#     name="Todo MCP Server",
# )

# @mcp.tool()
# async def add_task(user_id: str, title: str, description: Optional[str] = None):
#     async with get_async_session() as session:
#         todo = await crud.create_todo(
#             session=session,
#             title=title,
#             description=description,
#             owner_id=UUID(user_id),
#         )

#     return {
#         "id": str(todo.id),
#         "title": todo.title,
#         "completed": todo.completed,
#         "status": "created",
#     }


# @mcp.tool()
# async def list_tasks(user_id: str, status: Optional[str] = "all") -> List[dict]:
#     async with get_async_session() as session:
#         todos = await crud.get_todos_by_owner(session, UUID(user_id))

#     if status == "completed":
#         todos = [t for t in todos if t.completed]
#     elif status == "pending":
#         todos = [t for t in todos if not t.completed]

#     return [
#         {"id": str(t.id), "title": t.title, "completed": t.completed}
#         for t in todos
#     ]


# @mcp.tool()
# async def update_task(
#     user_id: str,
#     task_id: str,
#     title: Optional[str] = None,
#     description: Optional[str] = None,
#     completed: Optional[bool] = None,
# ):
#     async with get_async_session() as session:
#         todo = await crud.update_todo(
#             session=session,
#             todo_id=UUID(task_id),
#             owner_id=UUID(user_id),
#             title=title,
#             description=description,
#             completed=completed,
#         )

#     if not todo:
#         raise ValueError("Task not found")

#     return {
#         "id": str(todo.id),
#         "title": todo.title,
#         "completed": todo.completed,
#         "status": "updated",
#     }


# @mcp.tool()
# async def delete_task(user_id: str, task_id: str):
#     async with get_async_session() as session:
#         success = await crud.delete_todo(
#             session=session,
#             todo_id=UUID(task_id),
#             owner_id=UUID(user_id),
#         )

#     if not success:
#         raise ValueError("Task not found")

#     return {"id": task_id, "status": "deleted"}