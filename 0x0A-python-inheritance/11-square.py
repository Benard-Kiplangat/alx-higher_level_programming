#!/usr/bin/python3
"""Defines a class Square based on Rectangle class from 9-rectangle.py

Attributes:
    width (int): the width of the rectangle
    height (int): the height of the rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a Square base on Rectangle class

    Arguments: the Rectangle class
    """

    def __init__(self, size):
        """Initializes new instances of class Square

        Arguments:
        size: an integer width of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """A method that calculates the area of a square

        Returns: the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """The str method returns a string representation of the square

        Returns: a string representation of the square
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
