#!/usr/bin/python3

"""Base class module"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class base init function
            Args:
                id (int): id
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
