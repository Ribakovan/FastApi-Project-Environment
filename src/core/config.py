from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import BaseModel

load_dotenv()

BASE_DIR = Path(__file__).parent.parent


class Auth(BaseModel):
    PRIVATE_KEY: Path = BASE_DIR / "certs" / "private.pem"
    PUBLIC_KEY: Path = BASE_DIR / "certs" / "public.pem"
    ALGORITHM: str = "RS256"


class DbSettings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    @property
    def DATABASE_URL_ASYNCPG(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class Settings(BaseSettings):
    TITLE: str = "fastapi app"
    VERSION: str = "0.1.0"
    DOCS_URL: str = "/api/v1/docs"

    DEBUG: bool
    
    AUTH: Auth = Auth()
    DB: DbSettings = DbSettings()

    def api_settings(self) -> dict[str, any]:
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "docs_url": self.DOCS_URL,
            "debug": self.DEBUG
        }


settings = Settings()

