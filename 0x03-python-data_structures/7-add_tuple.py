#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """function that adds two tuples

    Returns a tuple with 2 integers
    """

    t_a_len = len(tuple_a)
    t_b_len = len(tuple_b)

    if t_a_len == 0:
        a1 = 0
        a2 = 0
    elif t_a_len == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if t_b_len == 0:
        b1 = 0
        b2 = 0
    elif t_b_len == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    new_tuple = (a1 + b1, a2 + b2)

    return (new_tuple)
