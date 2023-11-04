#!/usr/bin/python3
    """
    replace the element at index idx
    ...

    parameters
    ----------
    my_list: list
        list of integer
    idx: integer
        given infex

    Return:
        The element when found
        None if the index is negative
        None if the index is larger than the list length
    """
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for x in range(len(my_list)):
            if x == idx:
                my_list[x] = element
                break
        return my_list
