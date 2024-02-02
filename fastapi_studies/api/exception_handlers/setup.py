from fastapi import FastAPI

from fastapi_studies.application.movie.exceptions import MoviesNotFound
from fastapi_studies.application.movie.exceptions import PageOutOfRange
from .movie import movies_not_found_cb, page_out_of_range_cb


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(MoviesNotFound, movies_not_found_cb)
    app.add_exception_handler(PageOutOfRange, page_out_of_range_cb)
