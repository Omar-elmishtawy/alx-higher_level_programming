#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position
    ...

    Parameters
    ----------
    my_list : list
        The list of elements
    idx : integer
        The given position
    element : the new element

    Return:
        The original list if idx is negative or
        if idx out of range (> len(my_list))
    """
    new_list = my_list
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
