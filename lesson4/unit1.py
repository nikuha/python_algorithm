"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
"""
from timeit import timeit
from functools import lru_cache


# вариант через рекурсию без кэширования
def recursion(n):
    if n == 1:
        return 1
    return recursion(n - 1) + (-0.5) ** (n - 1)


# вариант через рекурсию с кэшированием
@lru_cache()
def recursion_cache(n):
    if n == 1:
        return 1
    return recursion(n - 1) + (-0.5) ** (n - 1)


# вариант через цикл
def cycle(n):
    series_sum = 0
    current_element = 1
    for i in range(n):
        series_sum += current_element
        current_element /= -2
    return series_sum


# вариант 2 через цикл по формуле
def formula(n):
    return sum([(-0.5) ** i for i in range(0, n)])


elements_count = 20

print(recursion(elements_count))
print(recursion_cache(elements_count))
print(cycle(elements_count))
print(formula(elements_count))


print('Рекурсия без кэширования: ', timeit('recursion(elements_count)', globals=globals()))

# самый быстрый метод - рекурсия с кэширование элементов
print('Рекурсия c кэшированием: ', timeit('recursion_cache(elements_count)', globals=globals()))

print('Цикл: ', timeit('cycle(elements_count)', globals=globals()))
print('Формула: ', timeit('formula(elements_count)', globals=globals()))

