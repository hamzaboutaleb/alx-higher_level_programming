#!/usr/bin/python3
""" add integer function"""


def add_integer(a, b=98):
    """add two integers.
        Args:
            a (int): first number
            b (int): second number
        Raises:
            TypeError: if not both same type
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and isinstance(b, int):
        raise TypeError("b must be an integer")
    if not isinstance(a, int):
        a = int(a)
    if not isinstance(b, int):
        b = int(b)
    return a + b
