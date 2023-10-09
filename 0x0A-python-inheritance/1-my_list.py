#!/usr/bin/python3
"""A class that inherits from list"""


class MyList(list):
    """A class that inherits from the list class
        list (list): the list to sort in ascending order
    """
    def print_sorted(self):
        """A function that prints a list in ascending order.
        """
        list_ = self[:]
        list_.sort()
        print(list_)
