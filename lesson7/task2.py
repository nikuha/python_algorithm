from random import randint


def merge(left_list, right_list):
    if not len(left_list):
        return right_list
    if not len(right_list):
        return left_list
    
    result_list = []
    index_left = index_right = 0
    
    while len(result_list) < len(left_list) + len(right_list):
        if left_list[index_left] <= right_list[index_right]:
            result_list.append(left_list[index_left])
            index_left += 1
        else:
            result_list.append(right_list[index_right])
            index_right += 1

        if index_right == len(right_list):
            result_list += left_list[index_left:]
            break
        if index_left == len(left_list):
            result_list += right_list[index_right:]
            break
    return result_list


def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(merge_sort(array[:midpoint]), merge_sort(array[midpoint:]))


my_list = [randint(0, 50) for _ in range(0, 15)]
print(my_list)

print(merge_sort(my_list))
