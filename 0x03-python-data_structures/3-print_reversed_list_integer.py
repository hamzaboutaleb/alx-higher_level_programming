#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list = my_list if my_list not None else []
    for i in reversed(my_list):
        print("{:d}".format(i))
