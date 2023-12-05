#!/usr/bin/python3
"""module for my int"""


class MyInt(int):
    """class for my _init"""
    def __eq__(self, compare_to):
        return self.real != compare_to

    def __ne__(self, value):
        return self.real == value
