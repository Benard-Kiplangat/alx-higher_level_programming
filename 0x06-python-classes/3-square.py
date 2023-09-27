#!/usr/bin/python3
"""A class that defines a Square"""


class Square:
    """A class that defines a private size attribute for square"""

    def __init__(self, size=0):
        """the init function that initialize new Squares
            size (int): The size to define the size of the new squares
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size * self.__size
