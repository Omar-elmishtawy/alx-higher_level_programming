#!/usr/bin/python3

def roman_to_int(roman_string):
    Roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    i = 0

    if not isinstance(roman_string, str) or roman_string is None:
        return result

    for i in range(len(roman_string) - 1):
        if Roman.get(roman_string[i]) >= Roman.get(roman_string[i+1]):
            result = result + Roman.get(roman_string[i])
        else:
            result = result - Roman.get(roman_string[i])
    result = result + Roman.get(roman_string[len(roman_string) - 1])
    return result
