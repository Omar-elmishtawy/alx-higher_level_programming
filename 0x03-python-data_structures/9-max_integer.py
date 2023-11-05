#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    get the max integer from the list
    ...

    Parameters
    ---------
    my_list : list

    Return:
        max integer from the list
    """
    if len(my_list) == 0:
        return None
    max_integer = my_list[0]
    for i in my_list:
        if i > max_integer:
            max_integer = i
    return max_integer
