#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = []
    for i in range(len(matrix)):
        tmp = []
        for j in range(len(matrix[i])):
            tmp.append(matrix[i][j])
        matrix_square.append(tmp)

    return matrix_square
