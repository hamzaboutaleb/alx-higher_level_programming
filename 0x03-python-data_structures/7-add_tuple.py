#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    for i in range(2):
        if tuple_a[i]:
            new_tuple[i] += tuple_a[i]
        if tuple_b[i]:
            new_tuple[i] += tuple_b[i]
    return tuple(new_tuple)
