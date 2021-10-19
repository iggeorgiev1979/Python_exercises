from collections import deque


def merge(list_1: deque, list_2: deque):
    tmp = []
    while len(list_1) > 0 and len(list_2) > 0:
        if list_1[0] < list_2[0]:
            tmp.append(list_1.popleft())
        else:
            tmp.append(list_2.popleft())
    if list_1:
        tmp.extend(list_1)
    else:
        tmp.extend(list_2)
    return tmp


def merge_sort(symbols: list):
    middle = len(symbols) // 2
    if middle == 0:
        return symbols

    first_section = merge_sort(symbols[:middle])
    second_section = merge_sort(symbols[middle:])

    return merge(deque(first_section), deque(second_section))


symbols_list = [5, 4, 3, 2, 1]
print(merge_sort(symbols_list))
