#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    print reverse list
    ...

    Parameters
    ----------
    my_list : list optional
        The list of integers

    Return:
        None
    """
    if isinstance(my_list, list):
        rever = my_list
        rever.reverse()
    for i in rever:
        print("{:d}".format(i))
