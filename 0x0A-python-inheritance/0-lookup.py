#!/usr/bin/python3
"""A function that returns a lookup function"""


def lookup(obj):
    """A function that returns a list of available attributes and methods
    of an object

    obj: the object class
    Returns: a list of available attributes and methods of an object
    """
    return dir(obj)
