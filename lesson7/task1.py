from random import randint

my_list = [randint(-100, 100) for _ in range(0, 20)]
print(my_list)


for i in range(len(my_list) - 1):
    for j in range(len(my_list) - 1 - i):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
print(my_list)
