#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    add two tuples
    ...

    Parameters
    ---------
    tuple_a : tuple
        tuple of integer

    tuple_b : tuple
        tuple of integer

    Return:
        tuple with two elemnts first one
        is the summition of the first element
        from tuple_a and tuple_b, second element
        is the summition of the second elemnt
    """

    if len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    elif len(tuple_a) == 0:
        tuple_a = (0, 0)
    else:
        tuple_a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    elif len(tuple_b) == 0:
        tuple_b = (0, 0)
    else:
        tuple_b = (tuple_b[0], tuple_b[1])

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
