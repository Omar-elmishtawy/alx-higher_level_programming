#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = [[matrix[i][j]**2 for j in range(len(matrix[i]))]for i in range(len(matrix))]

    return matrix_squared
