#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    for el in my_list:
        if el % 2 == 0:
            new_list.append(el)
    return new_list
