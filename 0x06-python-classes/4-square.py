#!/usr/bin/python3
"""Square Class"""


class Square:
    """This is a class of square

    Args:
        size (int): size of square

    Attributes:
        size (int): size of square
    """
    def __init__(self, size=0):
        self.size(size)
 
    def area(self):
        "get area of the square"
        return (self.__size)**2

    @size.setter
    def size(self, value):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    @property
    def size(self):
        return self.__size
