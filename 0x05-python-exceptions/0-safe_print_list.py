#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    index = 0
    while index < x:
        try:
            print(my_list[index], end="")
            index++
        except IndexError:
            return index
    return index
