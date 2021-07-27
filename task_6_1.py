from random import randint
def create_matrix(n, m, a, b):
    matrix = []
    for i in range(n):
        matrix_row = []
        for j in range(m):
            matrix_row.append(randint(a, b))
        matrix.append(matrix_row)
    return matrix
def print_new_matrix(matrix):
    for i in matrix:
        print(i)
print_new_matrix(create_matrix(5,5,1,9))
