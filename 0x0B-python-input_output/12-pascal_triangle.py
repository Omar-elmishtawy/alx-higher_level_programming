#!/usr/bin/python3
"""pascal triangle module"""


def pascal_triangle(n):
    """print pascal triangle
        args:
            n(int): heigth of the triangle
    """
    if n <= 0:
        return [[]]
    ls = [[1]]
    for i in range(1, n):
        ls_tmp = []
        for j in range(len(ls[i-1])+1):
            if j == 0 or j == len(ls[i-1]):
                ls_tmp.append(1)
            else:
                ls_tmp.append(ls[i-1][j-1] + ls[i-1][j])
        ls.append(ls_tmp)
    return ls
