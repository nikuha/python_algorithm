"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

M = 5
N = 4
a = []
for i in range(N):
    b = []
    for j in range(M - 1):
        b.append(int(input(f'{i+1}-я строка {j+1}-й элемент: ')))
    b.append(sum(b))
    a.append(b)

for i in range(N):
    for j in range(M):
        print("{:>3}".format(a[i][j]), end=' ')
    print()
