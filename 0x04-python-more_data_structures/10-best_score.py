#!/usr/bin/python3

def best_score(a_dictionary):
    best_score = 0
    who = None

    if a_dictionary:
        for key in a_dictionary.keys():
            if a_dictionary[key] > best_score:
                best_score = a_dictionary[key]
                who = key
    return who
