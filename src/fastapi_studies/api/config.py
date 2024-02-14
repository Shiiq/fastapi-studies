from dataclasses import dataclass


@dataclass
class ApiConfig:

    title: str = "FastAPI+Redis. Small movie search pet project."
    description: str = """

        Allows you to search for movies by parameters such as genres and release years.
        With a little touch of Redis and a kind of pagination.

        Available years: 
            * 1902 - 2018

        Available genres:
            * action
            * adventure
            * animation
            * children
            * comedy
            * crime
            * documentary
            * drama
            * fantasy
            * film-noir
            * horror
            * imax
            * musical
            * mystery
            * romance
            * sci-fi
            * thriller
            * war
            * western
    """
