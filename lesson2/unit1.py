import operator

number1_message = 'Введите 1-е число: '
number2_message = 'Введите 2-е число: '
operator_message = 'Введите знак операции + - * / или 0 для выхода из программы: '
error_message = 'Ошибка! Введите один из символов + - * / 0: '
null_message = 'Деление на ноль невозможно!'
op_list = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

while True:
    my_operator = input(operator_message)
    while not my_operator in '0+-*/':
        my_operator = input(error_message)
    if my_operator == '0':
        break
    a = float(input(number1_message))
    b = float(input(number2_message))
    if my_operator == '/' and b == 0:
        print(null_message)
        continue
    print('Ответ: ', op_list[my_operator](a, b))
