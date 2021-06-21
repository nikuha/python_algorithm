"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

my_list = [randint(0, 100) for _ in range(10)]
print(*my_list)

min_el = min(my_list)
min_el_k = my_list.index(min_el)
max_el = max(my_list)
max_el_k = my_list.index(max_el)

print(f'Наименьшее {min_el}, наибольшее {max_el}')

keys = range(min_el_k + 1, max_el_k) if min_el_k < max_el_k else range(max_el_k + 1, min_el_k)

my_sum = 0
for i in keys:
    # print(my_list[i])
    my_sum += my_list[i]

print(f'Сумма: {my_sum}')
