#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ A function that prints x elements 
    of a list"""
    i = 0;
    try:
        while x:
            print(my_list[i], end = "")
            x = x - 1;
            i = i + 1
            if (x == 0):
                print("");
    except IndexError:
        pass
    return (i)
