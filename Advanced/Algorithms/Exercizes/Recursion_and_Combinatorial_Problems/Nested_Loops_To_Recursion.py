def loop(n: int, result=[]):
    if len(result) == n:
        print(*result, sep=' ')
        return
    for el in range(1, n + 1):
        result.append(el)
        loop(n)
        result.pop()


loop(2)
