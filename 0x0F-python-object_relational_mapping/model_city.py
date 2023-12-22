#!/usr/bin/python3
""" Defines the city model """

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ A file that contains class definition of city and links
    MySQL table city

    attributes:
        __tablename__: the table name of MySQL database to store cities
        id: represents a unique int, primary key, autogenarated
        name: a column that will represent state names, not null
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
