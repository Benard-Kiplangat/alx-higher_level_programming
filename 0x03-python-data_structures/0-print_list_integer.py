#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """a script that prints integers

    Prints one integer per line
    Doesn't import any module or cast integers to strings
    Assumes that the list contains only integers
    Uses str.format() to print
    """
    if my_list:
        for i in my_list:
            print("{:d}".format(i))
