from fastapi import FastAPI

from fastapi_studies.api.routers.movie.router import movie_router
from fastapi_studies.api.routers.user.router import user_router


def setup_routers(app: FastAPI):
    app.include_router(movie_router)
    app.include_router(user_router)
