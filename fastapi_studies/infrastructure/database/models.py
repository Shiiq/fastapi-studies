from sqlalchemy import ForeignKey, SmallInteger, String, UniqueConstraint
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.associationproxy import AssociationProxy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

GENRE_TABLENAME = "genre"
MOVIE_TABLENAME = "movie"
MOVIEGENRE_TABLENAME = "movie_genre"


class Base(DeclarativeBase):
    """Base DB model"""

    __abstract__ = True


class IDMixin:

    id: Mapped[int] = mapped_column(primary_key=True)


class Genre(IDMixin, Base):
    """Genre DB model"""

    __tablename__ = GENRE_TABLENAME

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )

    movies: Mapped[list["Movie"]] = relationship(
        back_populates="genres",
        secondary=MOVIEGENRE_TABLENAME
    )


class Movie(IDMixin, Base):
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

    genre: AssociationProxy[list[str]] = association_proxy(
        target_collection="genres",
        attr="name"
    )

    genres: Mapped[list["Genre"]] = relationship(
        back_populates="movies",
        secondary=MOVIEGENRE_TABLENAME
    )

    __table_args__ = (
        UniqueConstraint("title", "year", name="uq_title_to_year"),
    )


class MovieGenre(Base):
    """Association DB model to store movie's genre"""

    __tablename__ = MOVIEGENRE_TABLENAME

    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movie.id"),
        primary_key=True
    )

    genre_id: Mapped[int] = mapped_column(
        ForeignKey("genre.id"),
        primary_key=True
    )
