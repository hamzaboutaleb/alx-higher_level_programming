#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """print my name firstname last name.
    Args:
        first_name (str): first name
        last_name (str) : last name by defualt its empty string
    Raises:
        TypeError: if first_name or last_name not str type
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name != "":
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
