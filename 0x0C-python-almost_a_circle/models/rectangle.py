#!/usr/bin/python3
"""rectangle class module"""


from modesl.base import Base


class Rectangle(Base):
    """Rectangle shape class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init class function
        Args:
            width: width of rectangle
            height: height of rectangle
            x: position x
            y: position y
            id : id of rectangle
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, val):
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y;

    @y.setter
    def y(self, val):
        self.y = val
