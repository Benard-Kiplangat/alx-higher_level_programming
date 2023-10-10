#!/usr/bin/python3
"""A module that loads a JSON file and creates an object"""
import json


def load_from_json_file(filename):
    """A fuction that creates a string from a JSON file

      filename (str): the name of the JSON file

    Returns: an object
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
