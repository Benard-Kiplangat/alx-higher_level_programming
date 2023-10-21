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

    @property
    def height(self):
        """A function that retrieves the width of the rectangle

            Returns:
                height (int): the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A function that sets the width of the rectangle

            Arguments:
                value (int): the value of rectangle's height to set

            Raises:
                TypeError: raised when height is not an int
                ValueError: raised when height is negative or 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("heigh must be > 0")
        self.__height = value

    @property
    def x(self):
        """A function that retrives the x coodinate of the rectangle

        Returns:
            x (int): the value of x coordinate
        """
        return self.__x

    @x.setter
    def x(self, value):
        """A function that sets the value of x

        Arguments:
            value (int): the value of the x coordinate

        Raises:
            TypeError: raised if x is not an integer
            ValueError: raised if x is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """A function that retrives the value of y coordinate

        Returns:
            (y) int: the value of y coordinate
        """
        return self.__y

    @y.setter
    def y(self, value):
        """A fucntion that sets the value of the y coordinate

        Arguments:
            value (int): the value of y coordinate of the rectangle

        Raises:
            TypeError: raised if y is not an int
            ValueError: raised if y is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """A function that calculates the area of the rectangle

        Returns:
            area (int): the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """A function that overrides the __str__ method
        and prints the properties of the rectangle
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    def display(self):
        """A function that prints an instance of rectangle with #"""
        if self.__y > 0:
            for i in range(self.__y):
                print()
        for i in range(self.__height):
            for j in range(self.__width):
                if j == 0:
                    print(" " * self.__x, end="")
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """A function that updates properties with *args

            Arguments:
                *args (tuple): the list of non-keyworded argumensts
                **kwargs (dict): a dictionary of keyworded arguments
        """

        if args is not None and len(args) != 0:
            attribs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attribs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """A function that creates a dictionary representation
        of a Rectangle

        Returns:
            dict (dictionary) : the properties of a rectangle
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
