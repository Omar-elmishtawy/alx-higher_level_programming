#!/usr/bin/python3
"""
class named mylist
"""


class MyList(list):
    """Class inherts from list class"""
    def print_sorted(self):
        """print list sorted ascendingly"""
        ls = self.copy()
        ls.sort()
        print(ls)
