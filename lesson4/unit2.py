from timeit import timeit
from math import log


def eratosthenes(k):
    n = int(1.5 * k * log(k)) + 1

    a = [i if i != 1 else 0 for i in range(n)]
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    nn = 0
    b = 0
    for i in range(0, len(a)):
        if a[i] != 0:
            nn += 1
            b = a[i]
        if nn == k:
            break

    return b


def prime_number(k):
    prime = 0
    prime_i = 0
    i = 2
    while prime_i < k:
        d = 2
        while i % d != 0:
            d += 1
        if d == i:
            prime = i
            prime_i += 1
        i += 1
    return prime


print(prime_number(300))
print(eratosthenes(300))


print('Простой перебор: ', timeit('prime_number(300)', globals=globals(), number=500))

# работает в несколько раз быстрее
print('Метод Эратосфена: ', timeit('eratosthenes(300)', globals=globals(), number=500))
