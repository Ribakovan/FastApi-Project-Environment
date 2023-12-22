import uvicorn

from fastapi import FastAPI

from core import settings
from api_v1 import router


def create_application() -> FastAPI:
    application = FastAPI(
        **settings.api_settings()
    )

    application.include_router(
        router=router,
        prefix="/api/v1"
    )

    return application


app = create_application()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
