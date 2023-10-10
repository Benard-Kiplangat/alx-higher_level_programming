#!/usr/bin/python3
"""A class that defines a class BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    """The class BaseGeometry
    """
    def area(self):
        """A function for area
        Exception: raised if area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates input values
            name (str): the name of the object
            value (int): the value of the property
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
