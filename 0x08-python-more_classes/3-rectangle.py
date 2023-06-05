#!/usr/bin/python3
"""
Rectangle class module
"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Init Rectangle class.
        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """area of recatngle"""
    def area(self):
        return self.width * self.height
    """perimter of rectangle"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        
        rect = ""

        for i in range(self.height):
            for j in range(self.width):
                rect += "#"
            rect += "\n"
        return rect
