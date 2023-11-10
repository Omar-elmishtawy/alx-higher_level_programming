#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_elements = []
    for i in range(len(set_1)):
        if list(set_1)[i] == list(set_2)[i]:
            common_elements.append(list(set_1)[i])
    return common_elements
