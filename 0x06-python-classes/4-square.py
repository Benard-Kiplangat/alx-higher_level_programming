#!/usr/bin/python3
"""A class that defines a Square"""


class Square:
    """A class that defines a private size attribute for square"""

    def __init__(self, size=0):
        """the init function that initialize new Squares
            size (int): The size to define the size of the new squares
        """
        self.set_size(size)

    def set_size(self, size):
        """A setter to set size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    def get_size(self):
        return self.size

    def area(self):
        """Calculates the area of the square"""
        return self.size * self.size
