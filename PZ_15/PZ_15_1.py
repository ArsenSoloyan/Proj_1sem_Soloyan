#В матрице найти минимальный элемент в предпоследней строке.

from random import randint

m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От =", "До =")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
for i in matrix:
    print(*i)
print('Минимальный элемент в предпоследней строке:', min(matrix[m-2]))