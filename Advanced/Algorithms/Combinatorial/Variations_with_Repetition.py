def generate(symbols: list, size: int, index=0, result=[]):
    if index == size:
        print(" ".join(result))
        return
    for el in symbols:
        result.append(el)
        generate(symbols, size, index + 1, result)
        result.pop()


generate(["A", "B", "C"], 2)
