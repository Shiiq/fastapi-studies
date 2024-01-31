from fastapi import Request

from fastapi_studies.api.routers.movie.request import PaginationRequest
from fastapi_studies.api.routers.movie.response import MoviePaginatedResponse
from fastapi_studies.application.movie.models import MoviesList
from fastapi_studies.application.movie.models import MoviePagination

ITEMS_PER_PAGE = 15


class Paginator:

    def create_response(
            self, data_input: MoviesList, request: Request
    ) -> MoviePaginatedResponse:
        resp = MoviePaginatedResponse(
            page=...,
            movies=data_input.movies,
            total_movies_count=data_input.total_count,
            next_page=...,
            prev_page=...,
        )

        pass

    def get_paginate_params(
            self,
            pagination_input: PaginationRequest
    ) -> MoviePagination:
        start = (pagination_input.page - 1) * ITEMS_PER_PAGE
        end = start + ITEMS_PER_PAGE
        return MoviePagination(
            start=start, end=end, page=pagination_input.page
        )

    def create_next_link(self):
        pass

    def create_prev_link(self):
        pass

    pass
