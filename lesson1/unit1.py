number_string = input('Введите трехзначное число: ')

a, b, c = [int(i) for i in number_string]

print(f'Сумма чисел: {a + b + c}, Произведение {a * b * c}')