from fastapi import Request, status
from fastapi.responses import ORJSONResponse, JSONResponse

from fastapi_studies.application.movie.exceptions import MoviesNotFound
from fastapi_studies.application.movie.exceptions import PageOutOfRange


async def movies_not_found_cb(_: Request, error: MoviesNotFound):
    return ORJSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": error.msg}
    )


async def page_out_of_range_cb(_: Request, error: PageOutOfRange):
    return ORJSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": error.msg}
    )
