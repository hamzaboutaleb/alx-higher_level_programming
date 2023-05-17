#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return None
    romans = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    number = 0
    last_d = 0
    for digit in roman_string[::-1]:
        val = romans[digit]
        if val >= last_d:
            number += val
            last_d = val
        else:
            number -= val
    return number
