#!/usr/bin/python3

def print_square(size):
    """print square size
        Args:
            size (int): size of square
        Raises:
            TypeError: if size is not int   
            ValueError: if size negative
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
