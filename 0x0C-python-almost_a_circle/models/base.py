#!/usr/bin/python3

"""Base class module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class base init function
            Args:
                id (int): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dict):
        if list_dict is None or len(list_dict) == 0:
            return "[]"
        return json.dumps(list_dict)
