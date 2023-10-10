#!/usr/bin/python3
"""A module that returns JSON representation of an object"""
import json


def to_json_string(my_obj):
    """A function that returns JSON representation of a string
        my_obj (type): the object to examine

        Returns: a JSON string representation of the object
    """
    return json.dumps(my_obj)
