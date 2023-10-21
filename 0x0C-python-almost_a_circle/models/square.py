#!/usr/bin/python3
"""A class that inherits from the class rectangle to define
    the properties of the square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square is a Class that defines the properties of a square
    based on the class Rectangle
    
    Attributes:
        size (int): the width of the square
        x (int): x coordinates of the square
        y (int): y coordinates of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Init function to create an instance of the Square

        Arguments:
            size (int): width of the square
            x (int, optional): x coordinate, defaults to 0
            y (int, optional): y coordinate, defaults to 0
            id (int, optional): the identity of square,
                                defaults to None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """A function that retrieves the width property

            Returns: (int) the width of the rectangle
        """
        return self.width

    @size.setter
    def size(self, value):
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
        self.width = value
        self.height = value

    def __str__(self):
        """A function that overrides the __str__ method
        and prints the properties of the square 
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """A function that updates properties with *args

            Arguments:
                *args (tuple): the list of non-keyworded argumensts
                **kwargs (dict): a dictionary of keyworded arguments
        """

        if args is not None and len(args) != 0:
            attribs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attribs[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attribs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """A function that creates a dictionary representation
        of the Square

        Returns:
            dict (dictionary) : the properties of the Square
        """
        dictsqr = self.__dict__
        dict1["id"] = dictsqr['id']
        dict1["width"] = dictsqr['width']
        dict1["height"] = dictsqr['height']
        dict1["x"] = dictsqr['x']
        dict1["y"] = dictsqr['y']
        return (dict1)
