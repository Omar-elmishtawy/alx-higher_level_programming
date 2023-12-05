#!/usr/bin/python3
"""class student"""


class Student():
    """student class"""
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def to_json(self):
        return self.__dict__
