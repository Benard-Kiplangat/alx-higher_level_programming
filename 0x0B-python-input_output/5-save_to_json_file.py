#!/usr/bin/python3
"""A module that saves an object to a file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes Objects to a textfile using JSON representation

    my_obj (type): the Object to write to file
    filename (str): the name of the file
    Returns: JSON representation
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json_object = json.dumps(my_obj)
        f.write(json_object)
        f.close()
