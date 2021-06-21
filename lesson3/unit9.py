"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

M = 5
N = 6
a = [[randint(0, 100) for _ in range(M)] for _ in range(N)]

max_el = 0
for j in range(M):
    min_el = None
    for i in range(N):
        if (not min_el) or a[i][j] < min_el:
            min_el = a[i][j]
    if min_el > max_el:
        max_el = min_el


for i in range(N):
    for j in range(M):
        print("{:>3}".format(a[i][j]), end=' ')
    print()

print(f'{max_el = }')
