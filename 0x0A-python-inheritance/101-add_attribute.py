#!/usr/bin/env bash
"""A class that defines a function to add an attribute to an object"""


def add_attribute(obj, attr, value):
    """Add attribute adds an attribute to an object

    Arguments:
        obj: an object to add the attribute
        attr: the attribute to set(a string)
        value: the value of the attribute

    Raises:
        TypeError is raised if the attribute cannot be added to the object
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
