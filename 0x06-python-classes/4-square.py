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
        "set the size value

        Args:
            value (int): size of the square
        "
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def size(self):
        "get size"
        return self.__size
