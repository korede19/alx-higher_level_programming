#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        new_matriz = [i[:] for i in matrix]
        for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                        new_matriz[i][j] = matrix[i][j] ** 2
        return new_matriz
