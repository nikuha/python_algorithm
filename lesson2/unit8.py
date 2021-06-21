number_count = int(input('Введите количество чисел: '))
digit = int(input('Введите цифру для поиска: '))

count = 0
for i in range(number_count):
    el = int(input(f'Введите число №{i+1}: '))
    while el > 0:
        if el % 10 == digit:
            count += 1
        el //= 10

print(f'В последовательности {count} цифр "{digit}": ')
