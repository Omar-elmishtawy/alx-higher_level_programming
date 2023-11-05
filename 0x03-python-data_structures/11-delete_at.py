#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    check if element is divisible by two
    ...

    Parameters
    ---------
    my_list : list

    Return:
        list of bool
    """
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
