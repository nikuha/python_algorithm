from hashlib import sha1


def str_count(string):

    result = {}

    # подстроки
    for i in range(str_length := len(string)):
        for l in range(i + 1, str_length + 1):
            sub_string = string[i:l]
            # print(sub_string)
            if sub_string != string and sub_string not in result:
                result[sub_string] = 0

    # подсчет уникальных подстрок
    for sub_string in result:
        ss_hash = sha1(sub_string.encode("utf-8")).hexdigest()
        ss_length = len(sub_string)
        for i in range(str_length - ss_length + 1):
            subs_hash = sha1(string[i:i+ss_length].encode("utf-8")).hexdigest()
            if subs_hash == ss_hash:
                result[sub_string] += 1

    return result


my_string = input("Введите строку: ")
my_result = str_count(my_string)
print('Уникальные подстроки:', my_result)
print('Количество уникальных подстрок:', len(my_result))
