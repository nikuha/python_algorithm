"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

from random import randint

my_list = [randint(-100, 100) for _ in range(10)]
print(*my_list)

max_number = None
position = None
for k in range(len(my_list)):
    if my_list[k] < 0 and ((not max_number) or my_list[k] > max_number):
        max_number = my_list[k]
        position = k

print(f'Максимальное отрицательное число {max_number}, позиция {position}')
