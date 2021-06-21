from random import randint

# последовательность чисел с рандомным разрядом
series = [randint(0, pow(10, randint(1, 7))) for _ in range(10)]

print(*series)

max_order = 0
max_number = 0
for el in series:
    el_order = 0
    n = el
    while n > 0:
        el_order += 1
        n //= 10
    if el_order > max_order:
        max_order = el_order
        max_number = el

print('Максимальный разряд: ', max_order, ' Число: ', max_number)
