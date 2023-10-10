#!/usr/bin/python3
"""A module that appends a string to a textfile"""


def append_write(filename="", text=""):
    """A function that appends a string to a text file (UTF8)
    and returns the number of chars added

    filename (str, optional): the name of the file or "" by default
    text (str, optional): the string of text to write to file
                            or "" by default
    Returns: the number of characters appended to file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        """This method returns the number of characters appended"""
        return f.write(text)
