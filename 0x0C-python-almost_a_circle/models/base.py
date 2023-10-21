#!/usr/bin/python3
"""A base clase for the Rectangle and Square objects"""


class Base:
    """
    A base class for Rectangle and Square objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """A class constructor for the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
