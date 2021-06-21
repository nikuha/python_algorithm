from random import randint

x = randint(0, 100)
n = 0
answer = int(input('Угадайте число от 0 до 100 за 10 попыток: '))

while n < 9:
    if answer == x:
        print(f'Бинго! Количесво попыток: {n + 1}.')
        break
    elif answer > x:
        answer = int(input(' < '))
    else:
        answer = int(input(' > '))
    n += 1
else:
    print(f'Игра окончена! Вы не укадали за {n + 1} попыток.')
