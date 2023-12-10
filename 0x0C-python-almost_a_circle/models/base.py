#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id_=None):
        if id_ is not None:
            self.id = id_
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
