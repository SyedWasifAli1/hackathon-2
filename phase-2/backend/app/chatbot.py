# #  0. Importing the necessary libraries
# from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI

# import os
# from dotenv import load_dotenv, find_dotenv

# # 0.1. Loading the environment variables
# load_dotenv(find_dotenv())

# # 1. Which LLM Provider to use? -> Google Chat Completions API Service
# external_client: AsyncOpenAI = AsyncOpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# # 2. Which LLM Model to use?
# llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
#     model="gemini-2.5-flash",
#     openai_client=external_client
# )

# # 3. Creating the Agent
# agent: Agent = Agent(name="Assistant", model=llm_model)

# # 4. Running the Agent
# result = Runner.run_sync(starting_agent=agent, input="Welcome and motivate me to learn Agentic AI")

# print("AGENT RESPONSE: " , result.final_output)









# # mcp_server.py

# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from typing import Optional
# from uuid import UUID

# from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI

# import os
# from dotenv import load_dotenv, find_dotenv

# from app import crud
# from app.database import get_async_session

# # -----------------------------
# # 0. Load environment variables
# # -----------------------------
# load_dotenv(find_dotenv())
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# # -----------------------------
# # 1. External LLM Client
# # -----------------------------
# external_client: AsyncOpenAI = AsyncOpenAI(
#     api_key=GEMINI_API_KEY,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# # -----------------------------
# # 2. LLM Model
# # -----------------------------
# llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
#     model="gemini-2.5-flash",
#     openai_client=external_client
# )

# # -----------------------------
# # 3. Agent
# # -----------------------------
# agent: Agent = Agent(name="TodoAgent", model=llm_model)

# # -----------------------------
# # 4. APIRouter
# # -----------------------------
# router = APIRouter(prefix="/chatbot", tags=["chatbot"])

# # -----------------------------
# # 5. Pydantic Models for MCP Tools
# # -----------------------------
# class AddTaskInput(BaseModel):
#     user_id: str
#     title: str
#     description: Optional[str] = None

# class UpdateTaskInput(BaseModel):
#     user_id: str
#     task_id: str
#     title: Optional[str] = None
#     description: Optional[str] = None
#     completed: Optional[bool] = None

# class TaskResponse(BaseModel):
#     task_id: str
#     status: str
#     title: str

# # -----------------------------
# # 6. MCP-style endpoints
# # -----------------------------
# @router.post("/mcp/add_task", response_model=TaskResponse)
# async def add_task(input: AddTaskInput):
#     async with get_async_session() as session:
#         todo = await crud.create_todo(
#             session, title=input.title, description=input.description, owner_id=UUID(input.user_id)
#         )
#         return TaskResponse(task_id=str(todo.id), status="created", title=todo.title)

# @router.post("/mcp/list_tasks")
# async def list_tasks(user_id: str, status: Optional[str] = "all"):
#     async with get_async_session() as session:
#         todos = await crud.get_todos_by_owner(session, owner_id=UUID(user_id))
#         if status == "pending":
#             todos = [t for t in todos if not t.completed]
#         elif status == "completed":
#             todos = [t for t in todos if t.completed]
#         return [{"id": str(t.id), "title": t.title, "completed": t.completed} for t in todos]

# @router.post("/mcp/complete_task", response_model=TaskResponse)
# async def complete_task(user_id: str, task_id: str):
#     async with get_async_session() as session:
#         todo = await crud.update_todo(session, UUID(task_id), UUID(user_id), completed=True)
#         if not todo:
#             raise HTTPException(status_code=404, detail="Task not found")
#         return TaskResponse(task_id=str(todo.id), status="completed", title=todo.title)

# @router.post("/mcp/delete_task", response_model=TaskResponse)
# async def delete_task(user_id: str, task_id: str):
#     async with get_async_session() as session:
#         success = await crud.delete_todo(session, UUID(task_id), UUID(user_id))
#         if not success:
#             raise HTTPException(status_code=404, detail="Task not found")
#         return TaskResponse(task_id=task_id, status="deleted", title="Deleted task")

# @router.post("/mcp/update_task", response_model=TaskResponse)
# async def update_task(input: UpdateTaskInput):
#     async with get_async_session() as session:
#         todo = await crud.update_todo(
#             session,
#             todo_id=UUID(input.task_id),
#             owner_id=UUID(input.user_id),
#             title=input.title,
#             description=input.description,
#             completed=input.completed,
#         )
#         if not todo:
#             raise HTTPException(status_code=404, detail="Task not found")
#         return TaskResponse(task_id=str(todo.id), status="updated", title=todo.title)

# # -----------------------------
# # 7. Optional: Run Agent with Input (chatbot use)
# # -----------------------------
# @router.post("/mcp/run_agent")
# async def run_agent(user_input: str):
#     result = await Runner.run(agent, user_input)
#     return {"response": result.final_output}











# 📦 Import Required Libraries
import os
from dotenv import load_dotenv
from uuid import UUID
from typing import Optional
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
import json

from agents import (
    Agent,                           
    Runner,                          
    AsyncOpenAI,                     
    OpenAIChatCompletionsModel,      
    function_tool,                   
    set_tracing_disabled,            
)

from app import crud
from app.database import get_async_session

# 🌿 Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

# 🚫 Disable internal tracing/logging
set_tracing_disabled(disabled=True)

# 🌐 Initialize OpenAI-compatible async client
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL
)

# 🧠 Model initialization
model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

# 🛠️ Task Management Tools
@function_tool
async def add_task(user_id: str, title: str, description: Optional[str] = None) -> dict:
    async with get_async_session() as session:
        todo = await crud.create_todo(
            session, title=title, description=description, owner_id=UUID(user_id)
        )
        return {"task_id": str(todo.id), "status": "created", "title": todo.title}

@function_tool
async def list_tasks(user_id: str, status: Optional[str] = "all") -> list:
    async with get_async_session() as session:
        todos = await crud.get_todos_by_owner(session, owner_id=UUID(user_id))
        if status == "pending":
            todos = [t for t in todos if not t.completed]
        elif status == "completed":
            todos = [t for t in todos if t.completed]
        return [{"id": str(t.id), "title": t.title, "completed": t.completed} for t in todos]

@function_tool
async def update_task(user_id: str, task_id: str, title: Optional[str] = None, description: Optional[str] = None, completed: Optional[bool] = None) -> dict:
    async with get_async_session() as session:
        todo = await crud.update_todo(
            session, todo_id=UUID(task_id), owner_id=UUID(user_id),
            title=title, description=description, completed=completed
        )
        if not todo:
            return {"error": "Task not found"}
        return {"task_id": str(todo.id), "status": "updated", "title": todo.title}

@function_tool
async def complete_task(user_id: str, task_id: str) -> dict:
    return await update_task(user_id, task_id, completed=True)

@function_tool
async def delete_task(user_id: str, task_id: str) -> dict:
    async with get_async_session() as session:
        success = await crud.delete_todo(session, UUID(task_id), UUID(user_id))
        if not success:
            return {"error": "Task not found"}
        return {"task_id": task_id, "status": "deleted", "title": "Deleted task"}

# 🤖 Create Agent
agent: Agent = Agent(
    name="TodoAssistant",
    instructions=(
        "You are a helpful task assistant. "
     
    ),
    model=model,
    tools=[add_task, list_tasks, update_task, complete_task, delete_task],
)

# -----------------------------
# FastAPI APIRouter
# -----------------------------
router = APIRouter(prefix="/chatbot", tags=["chatbot"])

class ChatRequest(BaseModel):
    user_input: str

class ChatResponse(BaseModel):
    response: str

async def execute_tool_from_agent(agent_output: str) -> str:
    """Parse agent JSON output and call the correct tool."""
    try:
        data = json.loads(agent_output)
        func_name = data.get("function")
        arguments = data.get("arguments", {})

        tool = next((t for t in agent.tools if t.__name__ == func_name), None)
        if not tool:
            return f"Tool '{func_name}' not found"

        result = await tool(**arguments)
        return str(result)

    except Exception as e:
        return f"Error executing tool: {e}"

@router.post("/ask", response_model=ChatResponse)
async def ask_agent(request: ChatRequest):
    """Endpoint to query the TodoAssistant agent."""
    result = await Runner.run(agent, request.user_input)
    # Attempt to execute tool if agent returned JSON
    response_text = await execute_tool_from_agent(result.final_output)
    return ChatResponse(response=response_text)
