#!/usr/bin/python3
"""This is rectangle module"""


class Rectangle:
    """class for rectangle
        args:
            width (int): width of the rectangle
            height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """constructor of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of the size"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("wifth must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of heghit"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
