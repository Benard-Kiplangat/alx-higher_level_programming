#!/usr/bin/python3
""" Defines the state model """

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ A file that contains class definitionof State and links
    MySQL table states

    attributes:
        __tablename__: the table name of MySQL database to store
        id: represents a unique int, primary key, autogenarated
        name: a column that will represent state names, not null
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
