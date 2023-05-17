#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_el = set(my_list)
    total = 0
    for el in unique_el:
        total += el
    return total
