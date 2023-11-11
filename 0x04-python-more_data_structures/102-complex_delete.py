#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    a_dic_cp = a_dictionary.copy()
    for i in a_dic_cp.keys():
        if a_dictionary[i] == value:
            a_dictionary.pop(i)
    return a_dictionary
