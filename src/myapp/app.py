from contextlib import asynccontextmanager
from fastapi import FastAPI

from myapp.domains.boards.router import router as boards_router
from myapp.domains.columns.router import router as columns_router

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # startup code
#     yield
#     # shutdown code


def create_app() -> FastAPI:
    app = FastAPI(title="My App", version="0.1.0")
    app.include_router(boards_router)
    app.include_router(columns_router)
    return app