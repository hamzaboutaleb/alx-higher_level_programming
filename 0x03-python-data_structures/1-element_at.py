#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return Null
    if idx >= len(my_list):
        return Null
    return my_list[idx]
