from fastapi_studies.application.movie.common import CacheStorageKey
from fastapi_studies.application.movie.exceptions import MoviesNotFound
from fastapi_studies.application.movie.exceptions import PageOutOfRange
from fastapi_studies.application.movie.interfaces import MovieCache
from fastapi_studies.application.movie.interfaces import MovieReader
from fastapi_studies.application.movie.models import Movie
from fastapi_studies.application.movie.models import MoviesList
from fastapi_studies.application.movie.models import MovieFilterParams
from fastapi_studies.application.movie.models import MoviePaginationParams


class MovieFindService:

    def __init__(self, movie_cache: MovieCache, movie_reader: MovieReader):
        self._movie_cache = movie_cache
        self._movie_reader = movie_reader

    async def __call__(
            self,
            filter_params: MovieFilterParams,
            pagination_params: MoviePaginationParams,
    ) -> MoviesList:
        self._set_cache_key(filter_params)
        movies_list = await self._get_movies(filter_params, pagination_params)
        return movies_list

    def _set_cache_key(
            self,
            filter_params: MovieFilterParams
    ):
        """
        Generate and attach uniq REDIS key to data obj :class:`MovieFilterParams`
        """
        cache_key = self._generate_uniq_key(filter_params)
        filter_params.cache_key = cache_key

    def _generate_uniq_key(
            self,
            key_params: MovieFilterParams
    ) -> CacheStorageKey:
        return CacheStorageKey(
            "movies:"
            f"{'-'.join(key_params.genre) if key_params.genre else 'all'}:"
            f"{key_params.year_from}-{key_params.year_to}"
        )

    async def _get_from_db(
            self,
            filter_params: MovieFilterParams,
    ) -> list[Movie]:
        movies = list(
            await self._movie_reader.get_by_genre_and_year(filter_params)
        )
        # means that we don't have movies with these parameters
        if not movies:
            raise MoviesNotFound
        return movies

    async def _read_from_cache(
            self,
            key: CacheStorageKey,
            pagination_params: MoviePaginationParams | None = None
    ) -> list[Movie]:
        movies = list(await self._movie_cache.read(
            key=key, pagination_params=pagination_params
        ))
        return movies

    async def _write_to_cache(
            self,
            key: CacheStorageKey,
            movies: list[Movie]
    ) -> int:
        movies_count = await self._movie_cache.write(
            key=key, movies=movies
        )
        return movies_count

    def _check_start_param(
            self,
            items_total: int,
            start_item: int
    ):
        if start_item > items_total:
            raise PageOutOfRange

    async def _get_movies(
            self,
            filter_params: MovieFilterParams,
            pagination_params: MoviePaginationParams
    ) -> MoviesList:

        # check cache for number of movies by the key
        movies_count = await self._movie_cache.get_items_count(
            filter_params.cache_key
        )

        # means that the cache is empty
        if movies_count == 0:
            movies = await self._get_from_db(filter_params)

            # upload movies to the cache - return value is the number of movies
            movies_uploaded = await self._write_to_cache(
                key=filter_params.cache_key, movies=movies
            )

            # check that current pagination `start` param match with total number of movies
            self._check_start_param(
                items_total=movies_uploaded,
                start_item=pagination_params.start
            )
            return MoviesList(
                movies=movies[pagination_params.start:pagination_params.end],
                total_count=movies_uploaded,
                current_page=pagination_params.page
            )

        # this means that the cache is not empty
        else:
            # check that current pagination `start` param match with total number of movies
            self._check_start_param(
                items_total=movies_count,
                start_item=pagination_params.start
            )
            movies = await self._read_from_cache(
                key=filter_params.cache_key,
                pagination_params=pagination_params
            )
            return MoviesList(
                movies=movies,
                total_count=movies_count,
                current_page=pagination_params.page
            )
