from random import randint
n, m, a, b = int(input()),int(input()),int(input()),int(input())
matrix = []
for i in range(n):
    matrix_row = []
    for j in range(m):
        matrix_row.append(randint(a, b))
    matrix.append(matrix_row)
print(matrix)
# 2. Максимальный элемент матрицы
def max_element(matrix):
    dup = []
    for lists in matrix:
        maxi = max(lists)
        dup.append(maxi)
    return max(dup)
print(max_element(matrix))