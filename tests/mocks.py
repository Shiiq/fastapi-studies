from fastapi_studies.api.routers.movie.response import MovieResponse


data = {
    125: MovieResponse(
        id=125,
        title="Rob Roy",
        year=1995,
        genres=["romance", "drama", "action", "war"]
    ),
    5000: MovieResponse(
        id=5000,
        title="Protocol",
        year=1984,
        genres=["comedy", ]
    )
}


class FakeDB:

    data = data

    async def get_by_id(self, movie_id):
        return self.data.get(movie_id)


def get_db_repo() -> FakeDB:
    return FakeDB()
