#!/usr/bin/python3
"""A module that converts a JSON string to an python object"""
import json


def from_json_string(my_str):
    """A function that returns the object (Python data structure)
    represented by a JSON string

    my_str (str): json object to convert to Python object.
    Returns: a Python object
    """
    return json.loads(my_str)
