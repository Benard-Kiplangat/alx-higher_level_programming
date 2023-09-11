#!/usr/bin/python3

def max_integer(my_list=[]):
    """function that returns biggest integer in list

    If the list is empty, return None
    """

    lenn = len(my_list)

    if lenn == 0:
        return

    my_list.sort()

    return my_list[-1]
