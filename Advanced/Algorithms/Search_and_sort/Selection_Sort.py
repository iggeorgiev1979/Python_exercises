def selection_sort(symbols: list):
    for index in range(len(symbols)):
        tmp = symbols[index]
        tmp_index = index
        for second_index in range(index + 1, len(symbols)):
            if tmp > symbols[second_index]:
                tmp_index = second_index
                tmp = symbols[second_index]
        symbols[index], symbols[tmp_index] = symbols[tmp_index], symbols[index]
    return symbols


symbols_list = [int(el) for el in "13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86 44 51".split()]
print(selection_sort(symbols_list))
