#!/usr/bin/python3
"""Square Class"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Initialize square

        Args:
        size(int): size of square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __lt__(self, compare_to):
        return self.area() < compare_to.area()
    
    def __eq__(self, compare_to):
        return self.area() == compare_to.area()

    def __le__(self, compare_to):
        return self.area() <= compare_to.area()

    def __gt__(self, compare_to):
        return self.area() > compare_to.area()

    def __ge__(self, compare_to):
        return self.area() >= compare_to.area()


    @property
    def size(self):
        """get size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """get square area"""
        return (self.__size)**2

    def __str__(self):
        """print are of the square"""
        return str(self.area())