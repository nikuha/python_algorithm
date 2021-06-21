#  Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125

elements_count = int(input('Введите количество элементов последовательности: '))

# вариант через цикл
series_sum = 0
current_element = 1
for i in range(elements_count):
    series_sum += current_element
    current_element /= -2
print(series_sum)


# вариант через рекурсию
def series(n):
    if n == 0:
        return 1
    return series(n - 1) / -2


series_sum = 0
for i in range(elements_count):
    series_sum += series(i)
print(series_sum)
