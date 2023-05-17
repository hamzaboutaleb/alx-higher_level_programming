#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = set()
    new_set.add(set_1.difference(set_2))
    new_set.add(set_2.difference(set_2))
    return new_set
