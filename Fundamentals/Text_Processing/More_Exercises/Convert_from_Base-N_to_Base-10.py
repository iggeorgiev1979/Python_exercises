def calculate(d: str, b: int):
    result = 0
    x = 0
    for el in d[::-1]:
        result += int(el) * (b**x)
        x += 1
    return result


base, digits = input().split()
print(calculate(digits, int(base)))
