"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

for div in range(2, 10):
    counter = 0
    for n in range(2, 100):
        if not n % div:
            counter += 1
    print(f'Кратных числу {div}: {counter}')
