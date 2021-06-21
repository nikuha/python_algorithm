a = input('Введите 1-ю букву: ')
b = input('Введите 2-ю букву: ')

start = ord('a')
a_ord = ord(a)
b_ord = ord(b)

print(f'Позиция буквы {a}: {a_ord - start + 1}, позиция буквы {b}: {b_ord - start + 1}')
print('Между буквами символов:', abs(a_ord - b_ord) - 1)
