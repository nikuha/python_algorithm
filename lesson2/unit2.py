a = input('Введите натуральное число: ')

even_numbers = odd_numbers = 0
for i in a:
    if int(i) % 2:
        odd_numbers += 1
    else:
        even_numbers +=1

print(f'Четных чисел: {even_numbers}, нечетных: {odd_numbers}')
