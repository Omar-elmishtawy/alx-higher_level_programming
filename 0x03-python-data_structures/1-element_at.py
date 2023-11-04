#!/usr/bin/python3
def element_at(my_list, idx):
    """
    get elemnt at index
    ...

    Parameters
    ---------
    my_list : list
        The list of integer
    idx : integer
        indext to get the elemnt at

    Return:
        The element at index idx

    """
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        for x in range(len(my_list)):
            if x == idx:
                return my_list[x]
    
