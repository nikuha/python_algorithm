"""
4. Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

my_list = [randint(0, 10) for _ in range(20)]
print(*my_list)

counter = [0]*len(my_list)
max_count = 0

for k in range(len(my_list)):
    for i in range(len(my_list)):
        if my_list[k] == my_list[i]:
            counter[k] += 1
    if counter[k] >= max_count:
        max_count = counter[k]

max_numbers = []
for k in range(len(my_list)):
    if counter[k] == max_count and not my_list[k] in max_numbers:
        max_numbers.append(my_list[k])

print(f'Число(а) {max_numbers} встречаются {max_count} раз(а)')
