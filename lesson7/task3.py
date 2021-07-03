from random import randint


def median(lst, half):
    for i in range(half * 2 + 1):
        less = []
        more = []
        pivots = []
        for j in range(half * 2 + 1):
            if lst[j] < lst[i]:
                less.append(lst[j])
            elif lst[j] > lst[i]:
                more.append(lst[j])
            else:
                pivots.append(lst[j])

        if len(less) == len(more) or len(pivots) > abs(len(more) - len(less)):
            return lst[i]


n = randint(2, 7)
my_list = [randint(-100, 100) for _ in range(2 * n + 1)]

print(f'{n = }')
print(my_list)
print('Медиана: ', median(my_list, n))

# проверка
print('Проверка')
my_list = sorted(my_list)
print(my_list)
print('Медиана: ', my_list[n])
