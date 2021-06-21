print('Введите три числа')

a = float(input('Первое: '))
b = float(input('Второе: '))
c = float(input('Третье: '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)