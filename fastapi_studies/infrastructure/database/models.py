from sqlalchemy import SmallInteger, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

MOVIE_TABLENAME = "movie"
GENRE_TABLENAME = "genre"


class Base(DeclarativeBase):
    """Base DB model"""

    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class Movie(Base):
    """Movie DB model"""

    __tablename__ = MOVIE_TABLENAME

    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    year: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False,
    )

    # genres: Mapped[list["Genre"]] = relationship(
    #     argument="Genre",
    #     back_populates="movies"
    # )

    __table_args__ = (
        UniqueConstraint("title", "year", name="uq_title_to_year"),
    )


class Genre(Base):
    """Genre DB model"""

    __tablename__ = GENRE_TABLENAME

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )

    # movies: Mapped[list["Movie"]] = relationship(
    #     argument="Movie",
    #     back_populates="genres"
    # )
