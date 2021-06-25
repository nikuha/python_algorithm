from collections import namedtuple

Company = namedtuple('Company', 'name profit')
n = int(input("Количество предприятий: "))
companies = []
total_sum = 0
for i in range(n):
    name = input(f"{i + 1}-е предприятие: ")

    profits = []
    for j in range(4):
        profits.append(float(input(f"Прибыль за {j + 1}-й квартал: ")))

    profit = sum(profits) / 4
    total_sum += profit

    companies.append(Company(name=name, profit=profit))

avrg_profit = total_sum / n

print(f'Средняя прибыль: {avrg_profit}')

print('Предприятия с прибылью выше среднего: ')
for company in companies:
    if company.profit > avrg_profit:
        print(f'{company.name}, {company.profit}')

print('Предприятия с прибылью ниже среднего: ')
for company in companies:
    if company.profit < avrg_profit:
        print(f'{company.name}, {company.profit}')
