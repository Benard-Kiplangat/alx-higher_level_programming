#!/usr/bin/python3
"""A function that checks if an object is an istance of a class"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if the object is an instance of 
    or if the object is an instance of a class that inherited from
    the pecified class or False
    obj (a_class): object to check type
    a_class (type): type of type to check
    Returns: True or False
    """
    # print("---> obj type {}".format(type(obj)))
    # print("---> a_class type {}".format(type(a_class)))
    return isinstance(obj, a_class)
