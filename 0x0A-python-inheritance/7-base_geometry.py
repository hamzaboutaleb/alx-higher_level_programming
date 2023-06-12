#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """"validate value
             Args:
                name: name
                value: value
             Raises:
                TypeError: if value not a number
                ValueError: if value not > 0
        """
    if not isinstance(value, int):
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
