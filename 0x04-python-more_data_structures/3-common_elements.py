#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_elements = []
    min_list = [len(set_1) if len(set_1) < len(set_2) else len(set_2)]
    for i in range(len(min_list)):
        if list(set_1)[i] == list(set_2)[i]:
            common_elements.append(list(set_1)[i])
    return common_elements
