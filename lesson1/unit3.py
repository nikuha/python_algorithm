print('Введите координаты первой точки:')
x1 = float(input('x1 = '))
y1 = float(input('x2 = '))

print('Введите координаты второй точки:')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

if x1 == x2:
    print('Вычислить функцию невозможно!')
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1

    sign = '+' if(b >= 0) else '-'
    print(f'Уравнение функции y = {k} * x {sign} {abs(b)}')