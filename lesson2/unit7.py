from random import randint


def digital_sum(n):
    if n <= 1:
        return n
    return n + digital_sum(n - 1)


# проверяем для случайных чисел
for n in [randint(2, 100) for i in range(10)]:
    print('Число: ', n, 'Расчет по функции: ', digital_sum(n), 'Расчет по формуле: ', n * (n + 1) / 2)
