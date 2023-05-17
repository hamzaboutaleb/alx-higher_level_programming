#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    keys = list(a_dictionary.keys())
    max_val = a_dictionary.get(keys[0])
    key = keys[0]
    for k in a_dictionary:
        if a_dictionary[k] > max_val:
            max_val = a_dictionary[k]
            key = k
    return k
