#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    print matrix
    ...

    Parameters
    ----------
    matrix : list of lists
        matrix nxm
    Return:
        None
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{}".format(matrix[i][j]), end="")
            if j != (len(matrix) - 1):
                print(" ", end="")
        print()
