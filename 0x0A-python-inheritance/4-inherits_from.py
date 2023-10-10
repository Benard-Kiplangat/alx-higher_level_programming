#!/usr/bin/python3
"""Defines a function inherits_from()"""


def inherits_from(obj, a_class):
    """A function that returns True if the object is an instance of a class that inherited the class or False if not
    obj (a_class): the object to check type
    a_class (type): the type of type to check
    Returns: True or False
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
