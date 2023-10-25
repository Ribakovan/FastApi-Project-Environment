from fastapi import FastAPI


def create_application() -> FastAPI:
    application = FastAPI()

    return application


app = create_application()
