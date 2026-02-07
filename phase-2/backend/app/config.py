from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs, urlencode

# Load environment variables from .env file
load_dotenv()

def sanitize_database_url(url: str) -> str:
    """Remove problematic query parameters from database URL for asyncpg compatibility"""
    if "postgresql+asyncpg" in url and ("sslmode" in url or "channel_binding" in url):
        # Parse the URL
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)

        # Remove problematic parameters
        query_params.pop('sslmode', None)
        query_params.pop('channel_binding', None)

        # Reconstruct the URL without problematic parameters
        new_query = urlencode(query_params, doseq=True)
        new_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        if new_query:
            new_url += f"?{new_query}"

        return new_url

    return url

class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./todo_test.db")  # Using SQLite for testing
    jwt_secret: str = os.getenv("JWT_SECRET", "your-default-secret-key-change-in-production")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "10080"))  # 7 days default
    cors_origins: Optional[str] = os.getenv("CORS_ORIGINS", "http://localhost:3000")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "AIzaSyBwxz2GVZpYHkEwzmw1-DKpQdJBm-rxEkA")
    class Config:
        env_file = ".env"

    def __init__(self, **values):
        super().__init__(**values)
        # Sanitize the database URL after initialization
        self.database_url = sanitize_database_url(self.database_url)

settings = Settings()