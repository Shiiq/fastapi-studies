from fastapi import Request, status
from fastapi.responses import ORJSONResponse, Response

from fastapi_studies.application.movie.exceptions import ApplicationError
from fastapi_studies.application.movie.exceptions import MoviesNotFound
from fastapi_studies.application.movie.exceptions import PageOutOfRange


def movies_not_found_cb(_: Request, error: MoviesNotFound) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": error.msg}
    )


def page_out_of_range_cb(_: Request, error: PageOutOfRange) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": error.msg}
    )
