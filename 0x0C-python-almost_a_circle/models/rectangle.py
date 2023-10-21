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
