def generate(symbols: list, size: int, index=0, result=[]):
    if index == size:
        print(" ".join(result))
        return
    for el in symbols:
        if el not in result:
            result.append(el)
            generate(symbols, size, index + 1, result)
            result.pop()


generate(["A", "B", "C", "D"], 3)
