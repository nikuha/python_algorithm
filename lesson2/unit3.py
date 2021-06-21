a = input('Введите натуральное число: ')

a_len = len(a)
b = [a[a_len - i - 1] for i in range(a_len)]
print(''.join(b))
