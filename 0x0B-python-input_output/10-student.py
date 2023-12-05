#!/usr/bin/python3
"""class student"""


class Student():
    """student class"""
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation of Student.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
