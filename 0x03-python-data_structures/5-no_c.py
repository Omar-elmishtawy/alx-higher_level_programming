#!/usr/bin/python3
def no_c(my_string):
    """
    remove c from my_string
    ...
    parameters
    ----------
    my_string: str
        string to remove c from

    Retunr:
        string with no c
    """
    str1 = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            str1 = str1 + i
    return str1
