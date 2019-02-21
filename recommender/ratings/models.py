from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    budget = Column(Integer)
    genres = Column(Integer)
    original_language = (Integer)
    title = Column(String)
    summary = Column(String)
    popularity = Column(Float)
    revenue = Column(Integer)
    vote_average = Column(Float)
    vote_count = Column(Integer)

    # TODO: Add more attributes

    ratings = relationship('Rating', back_populates='movie')


class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    rating = Column(Float)
    created_at = Column(DateTime)
    movie_id = Column(Integer, ForeignKey('movies.id'))

    movie = relationship('Movie', back_populates='ratings')
