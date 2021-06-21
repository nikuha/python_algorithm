"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

my_list = [randint(0, 100) for _ in range(10)]
print(*my_list)

min_el = None
max_el = 0
min_k = 0
max_k = 0
for k in range(len(my_list)):
    if my_list[k] > max_el:
        max_el = my_list[k]
        max_k = k
    if (not min_el) or my_list[k] < min_el:
        min_el = my_list[k]
        min_k = k

my_list[min_k] = max_el
my_list[max_k] = min_el
print(*my_list)
