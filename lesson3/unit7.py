"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

from random import randint

my_list = [randint(0, 100) for _ in range(10)]
print(*my_list)

min1 = my_list[0]
min2 = my_list[1]
if min2 < min1:
    min1, min2 = min2, min1

for k in range(2, len(my_list)):
    if my_list[k] < min1:
        min2 = min1
        min1 = my_list[k]
    elif my_list[k] < min2:
        min2 = my_list[k]

print(f'{min1 = }, {min2 = }')
