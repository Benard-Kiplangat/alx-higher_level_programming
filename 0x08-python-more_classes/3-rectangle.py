#!/usr/bin/python3
"""A class that defines a class Rectangle"""


class Rectangle:
    """A class that defines the properties of rectangle

    Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the new instances of a rectangle

        Arguments:
            width (int): the width of rectangle or 0 if none
            height (int): the height of rectangle or 0 if none
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """A getter method to retrieve the width of the rectangle

        Returns: the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """A getter method to retrieve the height of the rectangle

        Returns: the height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """A setter method for width property of the rectangle

        Arguments:
            value (int): the width to set

        Raises:
            TypeError: raised when the width is not an int
            ValueError: raised when the width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """A setter method for the height property

        Args:
            value (int): the height of the rectangle

        Raises:
            TypeError: raised if the height provided is not an integer
            ValueError: raised when the height provided is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """A method that calculates the area of a rectangle

        Returns: area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """A method that calculates the perimeter of a rectangle

        Returns: perimeter of the rectangle
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """A method that overides the __str__ method and prints the rectangle
        with the character #

        Returns: the rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")
        rectangle.pop()

        return "".join(rectangle)
