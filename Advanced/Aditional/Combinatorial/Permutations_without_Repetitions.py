# def combine(symbols: list, index=0):
#     if index == len(symbols):
#         print(" ".join(symbols))
#         return
#     combine(symbols, index + 1)
#     for i in range(index + 1, len(symbols)):
#         symbols[index], symbols[i] = symbols[i], symbols[index]
#         combine(symbols, index + 1)
#         symbols[index], symbols[i] = symbols[i], symbols[index]


def combine(symbols: list, index=0, result=[], used=[]):
    if not result:
        result = [None] * len(symbols)
    if not used:
        used = [False] * len(symbols)
    if index == len(symbols):
        print(" ".join(result))
        return

    for i in range(len(symbols)):
        if not used[i]:
            result[index] = symbols[i]
            used[i] = True
            combine(symbols, index + 1, result, used)
            used[i] = False


text_input = ["A", "B", "C", "D"]
combine(text_input)
