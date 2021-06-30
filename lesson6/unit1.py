import sys

print('Введите длину сторон треугольника')
a = float(input('1-я сторона: '))
b = float(input('2-я сторона: '))
c = float(input('3-я сторона: '))

if a + b <= c or b + c <= a or a + c <= b:
    print('Треугольника с такими сторонами не существует')
elif a == b == c:
    print('Треугольник равносторонний')
elif a == b or b == c or c == a:
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')


variables_size = 0
for i in {a, b, c}:
    variables_size += sys.getsizeof(i)

print(f'Использовано памяти: {variables_size}')
# 24 * 3 = 72 байта
# OC  - 64bit
# Python 3.9.5
