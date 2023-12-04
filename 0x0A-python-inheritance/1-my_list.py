#!/usr/bin/python3
"""
class named mylist
"""

class MyList(list):
    def print_sorted(self):
        ls = self.copy()
        ls.sort()
        print(ls)
