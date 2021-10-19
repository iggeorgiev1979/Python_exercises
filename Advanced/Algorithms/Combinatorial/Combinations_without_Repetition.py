def generate(symbols: list, size: int, result=[], start=0):
    if len(result) == size:
        print(" ".join(result))
        return
    for i in range(start, len(symbols)):
        result.append(symbols[i])
        generate(symbols, size, result, i + 1)
        result.pop()


generate(["A", "B", "C", "D"], 2)

# len(symbols) = n
# len(result) = n
# Total count of all combinations = n!/(k!*(n-k)!)
