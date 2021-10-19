def generate(symbols: list, size: int, result=[], start=0):
    if len(result) == size:
        print(" ".join(result))
        return
    for i in range(start, len(symbols)):
        result.append(symbols[i])
        generate(symbols, size, result, i)
        result.pop()


generate(["A", "B", "C", "D"], 2)
