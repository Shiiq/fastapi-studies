from starlette.datastructures import URL

from fastapi_studies.api.routers.movie.request import PaginationRequest
from fastapi_studies.api.routers.movie.response import MoviePaginatedResponse
from fastapi_studies.application.movie.models import MoviesList
from fastapi_studies.application.movie.models import MoviePaginationParams

ITEMS_PER_PAGE = 10


class MoviePaginator:

    def create_response(
            self,
            base_url: URL,
            movies_data: MoviesList
    ) -> MoviePaginatedResponse:

        next_page = self._create_next_link(
            base_url=base_url,
            current_page=movies_data.current_page,
            total_items=movies_data.total_count,
        )
        prev_page = self._create_prev_link(
            base_url=base_url,
            current_page=movies_data.current_page
        )
        return MoviePaginatedResponse(
            current_page=movies_data.current_page,
            next_page=next_page,
            prev_page=prev_page,
            total_movies=movies_data.total_count,
            movies=movies_data.movies,
        )

    def get_params(
            self,
            pagination_input: PaginationRequest
    ) -> MoviePaginationParams:
        start = (pagination_input.page - 1) * ITEMS_PER_PAGE
        end = start + ITEMS_PER_PAGE
        return MoviePaginationParams(
            start=start, end=end, page=pagination_input.page
        )

    def _create_next_link(
            self,
            base_url: URL,
            current_page: int,
            total_items: int
    ) -> str | None:
        if current_page == (total_items // ITEMS_PER_PAGE + 1):
            return None
        return str(base_url.include_query_params(page=current_page+1))

    def _create_prev_link(
            self,
            base_url: URL,
            current_page: int
    ) -> str | None:
        if current_page == 1:
            return None
        return str(base_url.include_query_params(page=current_page-1))
