#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)
    """

    new_list = list(set(my_list))
    result = 0

    for num in new_list:
        result += num
    return result
