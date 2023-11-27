#!/usr/bin/python3
"""This is rectangle module"""


class Rectangle:
    """class for rectangle
        args:
            width (int): width of the rectangle
            height (int): height of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """constructor of the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calcuate perimeter for rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0 or self.print_symbol == "":
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print(self.print_symbol, end="")
            if i != self.__height - 1:
                print()
        return ""

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        "detect deletion of object"
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area
        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance different from rect_1
        Returns:
            The instance with the biggest area,
            or rect_1 if both rectangles have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
