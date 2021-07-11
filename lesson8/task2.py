from collections import deque


# Узел дерева
class MyNode:
    def __init__(self, value, symbol=None, left=None, right=None):
        self.value = value
        self.symbol = symbol
        self.left = left
        self.right = right


# крайний правый символ и путь до него
def search(node, path=''):
    if node.symbol is not None:
        node.value = 0
        return node.symbol, path
    if node.right is not None and node.right.value != 0:
        spam = search(node.right, path=f'{path}1')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam
    if node.left is not None and node.left.value != 0:
        spam = search(node.left, path=f'{path}0')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam


def transfer_table(my_string):
    # перевод строки в словарь символов
    s_dict = {}
    for i in my_string:
        if i not in s_dict:
            s_dict[i] = 1
        else:
            s_dict[i] += 1
    node_list = deque([MyNode(s_dict[i], i) for i in s_dict])

    for i in range(len(s_dict)-1):
        node_list = deque(sorted(node_list, key=lambda node: node.value))

        first_el = node_list.popleft()
        second_el = node_list.popleft()

        new_node = MyNode(value=first_el.value + second_el.value, left=first_el, right=second_el)

        node_list.appendleft(new_node)

    tree = node_list[0]

    # таблица перевода
    table = {}
    for _ in range(len(s_dict)):
        k = search(tree)
        table[k[0]] = k[1]

    return table


s = 'из трех символов'
my_table = transfer_table(s)

print(f'Строка: {s}')

# Переводим
print('Кодированная строка:')
for char in s:
    print(my_table[char], end=' ')
