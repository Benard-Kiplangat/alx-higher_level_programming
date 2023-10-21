#!/usr/bin/python3
"""A class that inherits from the base class"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle is a Class that defines the properties of a Rectangle
    
    Attributes:
        width (int): the width
        height (int): the height
        x (int): x coordinates
        y (int): y coordinates
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init function to create an instance of Rectangle

        Arguments:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x coordinate, defaults to 0
            y (int, optional): y coordinate, defaults to 0
            id (int, optional): the identity of rectangle, defaults to None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """A function that retrieves the width property

            Returns: (int) the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A function that sets the width of the rectangle

        Arguments:
            value (int): the value of the width to set to

        Raises:
            TypeError: raised when width is not an int
            ValueError: raised when width is 0 or negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
