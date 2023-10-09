#!/usr/bin/python3
"""A function that checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """a function that checks if an object is exactly an instance of a
    specified class

    obj (a_class): the object to check its type
    a_class (type): the type of type to check
    Returns: True or False
    """
    return type(obj) == a_class
