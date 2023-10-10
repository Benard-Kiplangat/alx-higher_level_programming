#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8)
    and returns the number of characters written

    filename (str, optional): the name of the file or "" by default
    text (str, optional): the string of text to write to file or "" by default

    Returns: the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """This method returns the number of characters written"""
        return f.write(text)
