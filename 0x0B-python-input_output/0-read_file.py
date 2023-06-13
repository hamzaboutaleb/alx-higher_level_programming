#!/usr/bin/python3

"""read file module"""


def read_file(filename=''):
    """read file
        Args:
            filename: ""filename
    """
    with open(filename, encoding="utf-8) as file:
        print(file.read())
