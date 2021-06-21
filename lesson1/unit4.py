from random import random, randint

a = int(input('Введите диапазон целых чисел от '))
b = int(input('до '))
x = randint(a, b)
print(f'Случайное целое число: {x}')

a = float(input('Введите диапазон вещественных чисел от '))
b = float(input('до '))
x = random() * (b - a) + a
print(f'Случайное вещественное число: {x}')

a = ord(input('Введите символ от '))
b = ord(input('до '))
x = int(random() * (b - a)) + a
print(f'Случайный символ: {chr(x)}')

