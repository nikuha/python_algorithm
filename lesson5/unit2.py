from collections import deque

hex_symbols = '0123456789ABCDEF'
hex_to_dex = {hex_symbols[i]: i for i in range(len(hex_symbols))}


class MyHex:
    def __init__(self, init_dex=0, init_hex=None):
        if init_hex:
            self.hex = list(init_hex)  # 16-ричное строчное представление
            dex = 0
            my_deque = deque(init_hex)
            my_deque.reverse()
            for i in range(len(my_deque)):
                dex += hex_to_dex[my_deque[i]] * 16 ** i
            self.dex = dex  # десятичное представление
        else:
            self.dex = init_dex
            my_deque = deque()
            while init_dex > 0:
                d = init_dex % 16
                for i in hex_symbols:
                    if hex_to_dex[i] == d:
                        my_deque.append(i)
                init_dex //= 16
            my_deque.reverse()
            self.hex = list(my_deque)

    def __add__(self, other):
        return MyHex(init_dex=self.dex + other.dex)

    def __mul__(self, other):
        return MyHex(init_dex=self.dex * other.dex)

    def __str__(self):
        return f'hex: {self.hex}, dex: {self.dex}'


num_1 = MyHex(init_hex=input('1-е число в 16-ричном формате: ').upper())
num_2 = MyHex(init_hex=input('2-е число в 16-ричном формате: ').upper())
print('1-е число ', num_1)
print('2-е число ', num_2)
print('Сумма ', num_1 + num_2)
print('Произведение ', num_1 * num_2)

