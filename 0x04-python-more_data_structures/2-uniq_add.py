#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    visited = set()
    for el in my_list:
        if el in visited:
            continue
        new_list.append(el)
        visited.add(el)
    return new_list
