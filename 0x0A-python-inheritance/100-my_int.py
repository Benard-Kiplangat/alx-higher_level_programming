#!/usr/bin/python3
"""The class MyInt that inherits from int"""


class MyInt(int):
    """The class MyInt

    Arguments: int (int): the value
    """
    def __init__(self, value):
        """Initializes new instances of MyInt

        Arguments: integer value
        """
        self.__value = value

    def __eq__(self, other):
        """Checks if value provided is equal to other

        Arguments: the other integer to be compared

        Returns: True or False
        """
        return self.__value != other

    def __ne__(self, other):
        """Checks if value provided is not equal to other

        Arguments: the other integer

        Returns: True or False
        """
        return self.__value == other
