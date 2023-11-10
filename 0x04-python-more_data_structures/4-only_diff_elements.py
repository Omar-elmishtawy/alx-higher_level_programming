#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_elements = []
    for i in set_1:
        for j in set_2:
            if i != j:
                diff_elements.append(i)
    diff_elements = list(set(diff_elements))
    return diff_elements
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
