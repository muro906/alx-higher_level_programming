#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    try:
        if len(matrix) == 0:
            print("{}".format('$'))
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if j == cols - 1:
                    print("{:d}".format(matrix[i][j]), end="")
                else:
                    print("{:d} ".format(matrix[i][j]), end="")
            print("{}".format('$'))
    except TypeError:
        pass
