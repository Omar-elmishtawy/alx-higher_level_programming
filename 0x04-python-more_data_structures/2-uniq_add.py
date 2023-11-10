#!/usr/bin/python3
def uniq_add(my_list=[]):
    dic = {}
    result = 0

    for i in my_list:
        if i not in dic:
            result = result + i
            dic[i] = True
    return result

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
