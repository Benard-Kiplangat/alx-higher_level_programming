#!/usr/bin/python3
"""A function read_file to read files"""


def read_file(filename=""):
    """A function that reads a file and prints to stdout
        filename (str, optional): name of file to read or "" on default
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
