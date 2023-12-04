#!/usr/bin/python3
"""check if object is exactly instance of class"""


def inherits_from(obj, a_class):
    """check if obj is same class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
