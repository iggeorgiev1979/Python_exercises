def combine(symbols: list, index=0):
    if index == len(symbols):
        print(" ".join(symbols))
        return
    combine(symbols, index + 1)
    for i in range(index + 1, len(symbols)):
        symbols[index], symbols[i] = symbols[i], symbols[index]
        combine(symbols, index + 1)
        symbols[index], symbols[i] = symbols[i], symbols[index]


text_input = ["A", "B", "C"]
combine(text_input)
