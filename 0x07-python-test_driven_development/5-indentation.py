#!/usr/bin/python3
"""Defines a function that prints a text with 2 new lines after each,
    of these characters: . ? and :
    text_indentation: a function that prints a text with specific conditions
"""


def text_indentation(text):
    """Prints a text with 2 new lines after .?: characters
        text (str): string to be examined
    Raises:
        TypeError: text is not str
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
