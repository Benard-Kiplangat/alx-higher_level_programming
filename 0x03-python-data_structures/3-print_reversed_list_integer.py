#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """a script that prints integers

    Prints one integer per line
    Doesn't import any module or cast integers to strings
    Assumes that the list contains only integers
    Uses str.format() to print
    """
    if my_list:
        i = 0
        lenn = len(my_list) - 1
        while lenn >= i:
            print("{:d}".format(my_list[lenn]))
            lenn = lenn - 1
