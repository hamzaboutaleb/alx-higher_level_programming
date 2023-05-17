#/usr/bin/python3

def common_elements(set_1, set_2):
    new_set = set()
    for el in set_1:
        if el in set_2:
            new_set.add(el)
            set_2.remove(el)
    return new_set
