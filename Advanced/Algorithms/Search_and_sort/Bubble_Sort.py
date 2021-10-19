def bubble_sort(symbols: list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for index in range(len(symbols) - 1):
            if symbols[index] > symbols[index + 1]:
                symbols[index], symbols[index + 1] = symbols[index + 1], symbols[index]
                is_sorted = False

    return symbols


symbols_list = "5 4 3 3 2 1".split()
print(bubble_sort(symbols_list))
