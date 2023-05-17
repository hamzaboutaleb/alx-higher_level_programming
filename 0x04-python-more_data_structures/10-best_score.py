#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    keys = a_dictionary.keys()
    max_val = a_dictionary[keys[0]]
    key = keys[0]
    for k in keys:
        if a_dictionary[k] > max_val:
            max_val = a_dictionary[k]
            key = k
    return k
