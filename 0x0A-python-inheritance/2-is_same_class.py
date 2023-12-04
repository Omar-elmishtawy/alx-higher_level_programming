#!/usr/bin/python3
"""check if object is exactly instance of class"""


def is_same_class(obj, a_class):
    """check if obj is same class"""
    if type(obj) == a_class:
        return True
    else:
        return False
