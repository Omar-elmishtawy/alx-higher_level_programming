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
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
