#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_elements = []
    for i in range(len(set_1)):
        if set_1[i] == set_2[j]:
            common_elements.append(set_1[i])
    return common_elements
