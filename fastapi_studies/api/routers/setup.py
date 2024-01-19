from fastapi import FastAPI

from .movies import movies_router
from .users import users_router


def setup_routers(app: FastAPI):
    app.include_router(movies_router)
    app.include_router(users_router)
