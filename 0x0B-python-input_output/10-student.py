#!/usr/bin/python3
"""class student"""


class Student():
    """student class"""
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        elif for atr in attrs:
            if type(atr) is not str:
                return self.__dict__
        else:
            dic = {}
            for i in range(len(attrs)):
                for atr in self.__dict__:
                    if attrs[i] == atr:
                        dic[atr] = self.__dict__[atr]
            return dic
