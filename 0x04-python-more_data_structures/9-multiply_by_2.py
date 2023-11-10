#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dicct = {}
    for key in a_dictionary.keys():
        dicct[key] = a_dictionary.get(key) * 2
    return dicct
