#!/usr/bin/python3

"""Defines a function add_integer(a, b=98)
    that adds two integers.
"""

def add_integer(a, b=98):
    """ A function that adds two integer and/or float values
    Arguments:
        a (int): First value
        b (int): Optional second value, by default its value is98
    Raises:
        TypeError: If a and b are not either floats or integers
    Return:
        int: Sum of a and b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return (a + b)
