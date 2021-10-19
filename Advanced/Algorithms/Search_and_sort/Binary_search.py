def binary(search, symbols):
    low = 0
    high = len(symbols) - 1
    result = None
    while not result:
        if high < low:
            break
        index = low + (high - low) // 2
        if search == symbols[index]:
            result = index
        if symbols[index] < search:
            low = index + 1
        else:
            high = index - 1
    return index


symbols_list = [int(el) for el in "-1 0 1 2 4".split()]
symbol_to_search = 1

print(f"Index of {symbol_to_search} is {binary(symbol_to_search, symbols_list)}")
