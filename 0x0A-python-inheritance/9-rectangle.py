#!/usr/bin/python3
"""A class that defines a class Rectangle based on 8-base_geometry.py

Attributes:
    width (int): the width of the rectangle
    height (int): the height of the rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Initilizes new instances of Rectangle

        Args:
            width (int): the width of rectangle
            height (int): the height of rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """a method that calculates the area of a rectangle

        Returns: the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Overides the __str__ method to return a string
        representation of the rectangle

        Returns: a string representation of rectangle
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
