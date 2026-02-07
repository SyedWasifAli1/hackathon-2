# chatbot.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

# Agent imports
from agents import Agent, Runner, OpenAIChatCompletionsModel,AsyncOpenAI

import os
from dotenv import load_dotenv, find_dotenv

from app import crud
from app.database import get_async_session

# --------------------------------------
# 0. Load environment for OpenRouter
# --------------------------------------
load_dotenv(find_dotenv())

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# --------------------------------------
# 1. External OpenRouter client
# --------------------------------------
# openrouter_client = OpenAI(
#     api_key=OPENROUTER_API_KEY,
#     base_url=OPENROUTER_BASE_URL,
#     default_headers={
#         "HTTP-Referer": os.getenv("APP_URL", ""),   # Optional but recommended
#         "X-Title": os.getenv("APP_NAME", "TodoAI")  # Optional
#     }
# )
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=os.getenv("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"),
    base_url="https://openrouter.ai/api/v1"
)
# --------------------------------------
# 2. LLM Model via OpenRouter
# --------------------------------------
llm_model = OpenAIChatCompletionsModel(
    model="openai/gpt-4-turbo",  # You can choose any OpenRouter supported model
    openai_client=external_client
)

# --------------------------------------
# 3. Create the Agent
# --------------------------------------
agent = Agent(name="TodoAssistant", model=llm_model)

# --------------------------------------
# 4. FastAPI setup
# --------------------------------------
app = FastAPI(title="Todo AI Chatbot (OpenRouter)")

class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None

@app.post("/api/{user_id}/chat")
async def chat_endpoint(user_id: str, request: ChatRequest):
    user_uuid = UUID(user_id)

    async with get_async_session() as session:
        # Create conversation if not provided
        if not request.conversation_id:
            conv = await crud.create_conversation(session, user_uuid)
            conversation_id = str(conv.id)
        else:
            conv = await crud.get_conversation(session, UUID(request.conversation_id))
            conversation_id = str(conv.id)

        # Save user message
        await crud.add_message(
            session, UUID(conversation_id), user_uuid, role="user", content=request.message
        )

        # Fetch history
        messages = await crud.get_messages(session, UUID(conversation_id))
        history_text = "\n".join([f"{m.role}: {m.content}" for m in messages])
        prompt = f"{history_text}\nuser: {request.message}"

        # Run the agent
        result = await Runner.run(agent, prompt)

        # Save assistant response
        await crud.add_message(
            session, UUID(conversation_id), user_uuid, role="assistant", content=result.final_output
        )

        return {
            "conversation_id": conversation_id,
            "response": result.final_output
        }