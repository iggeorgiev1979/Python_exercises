def calculate(n: int, b: int):
    result = []
    while not n == 0:
        el = n % b
        result.append(str(el))
        n //= b
    return ''.join(reversed(result))


base, number = input().split()
print(calculate(int(number), int(base)))
