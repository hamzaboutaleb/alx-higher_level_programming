#!/usr/bin/python3
"""square module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """init squre"""
        self.__size = size
        super().__init__(self.__size, self.__size)
