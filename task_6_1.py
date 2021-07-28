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
# 3. Минимальный элемент матрицы
def min_element(matrix):
    dup2 = []
    for lists in matrix:
        mini = min(lists)
        dup2.append(mini)
    return min(dup2)
print(min_element(matrix))
# 4. Сумма всех элементов матрицы
def summ_element(matrix):
    total = 0
    for i in range(len(matrix)):
        total += sum(matrix[i])
    return total
print(summ_element(matrix))
# 5. Индекс ряда с максимальной суммой
def index_max_sum(matrix):
    summ_row = []
    for i in range(len(matrix)):
        summ_row.append(sum(matrix[i]))
    return summ_row.index(max(summ_row))
print(index_max_sum(matrix))
# 6. Индекс колонки с максимальной суммой
def index_column_maxsum(matrix):
    summ_column = []
    for i in range(len(matrix)):
        t = 0
        for j in matrix:
            t+= j[i]
        summ_column.append(t)
    return summ_column.index((max(summ_column)))
print(index_column_maxsum(matrix))
# 7. Индекс ряда с минимальной суммой
def index_min_sum(matrix):
    summ_row = []
    for i in range(len(matrix)):
        summ_row.append(sum(matrix[i]))
    return summ_row.index(min(summ_row))
print(index_min_sum(matrix))
# 8. Индекс колонки с минимальной суммой
def index_column_minsum(matrix):
    summ_column = []
    for i in range(len(matrix)):
        t = 0
        for j in matrix:
            t+= j[i]
        summ_column.append(t)
    return summ_column.index((min(summ_column)))
print(index_column_minsum(matrix))
# 9. Обнуление элементов выше главной диагонали
def zero_hight(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j]=0
    for i in matrix:
        print(i)
zero_hight(matrix)
print()
# 10. Обнуление элементов ниже главной диагонали
def zero_bellow(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < i:
                matrix[i][j] = 0
    for i in matrix:
        print(i)
zero_bellow(matrix)
# 11. Создание двух новых матриц:
def new_matrix_a(x, y, c, d):
    matrix_a = [[randint(c,d) for i in range(x)]for j in range(y)]
    matrix_b = [[randint(c, d) for i in range(x)] for j in range(y)]
    print(matrix_a)
    print(matrix_b)
new_matrix_a(3,3,1,9)
