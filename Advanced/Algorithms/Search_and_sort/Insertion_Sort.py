def insertion_sort(symbols: list):
    for i in range(len(symbols)):
        number_1 = symbols[i]
        tmp = None
        for index in range(i - 1, - 1, -1):
            number_2 = symbols[index]
            if number_1 < number_2:
                tmp = index
        if tmp is not None:
            symbols.insert(tmp, symbols.pop(i))

    return symbols


print(insertion_sort([int(el) for el in "13 93 37 74 61 65 5 55".split()]))
