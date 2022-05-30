from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI app"
    APP_DB: str = None

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
