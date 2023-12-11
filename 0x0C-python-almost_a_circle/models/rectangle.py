#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Initialize a new Rectangle.

    Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        x (int): The x coordinate of the new Rectangle.
        y (int): The y coordinate of the new Rectangle.
        id (int): The identity of the new Rectangle.
    Raises:
        TypeError: If either of width or height is not an int.
        ValueError: If either of width or height <= 0.
        TypeError: If either of x or y is not an int.
        ValueError: If either of x or y < 0.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        "initilization for the rectangle"
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate_attributes_int(self, name, side, x_y=False):
        if not isinstance(side, int):
            raise TypeError("{} must be integer".format(name))
        if not x_y:
            if side <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if side < 0:
                raise ValueError("{} must be >=0".format(name))

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.__validate_attributes_int("width", width)
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter
        """
        self.__validate_attributes_int('height', height)
        self.__height = height

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """x setter
        """
        self.validate_attributes_int('x', x, True)
        self.__x = x

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """y setter
        """
        self.validate_attributes_int('y', y, True)
        self.__y = y

    def area(self):
        """calculate area of rectangle"""
        return self.width * self.height

    def display(self):
        "display the rectangle"
        print(self.y * "\n", end="")
        for i in range(self.height):
            print(self.x * " ", end="")
            print(self.width * "#")

    def __str__(self):
        "return rdctangle"
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        "Update the rectangle"
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except Exception as e:
            pass

    def to_dictionary(self):
        "return the rectangle as dictionary"
        return ({'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y})
