from fastapi import FastAPI

from .users import users_router


def setup_routers(app: FastAPI):
    app.include_router(users_router)
