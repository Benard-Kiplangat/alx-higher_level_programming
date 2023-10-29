#!/usr/bin/python3
"""A class Rectangle based on 7-base_geometry.py
    width (int): the width of the rectangle
    height (int): the height of the rectangl
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class Rectangle based on BaseGeometry"""

    def __init__(self, width, height):
        """A function that creates new instances of Rectangle
            width (int): the width of rectangle
            height (int): the height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
