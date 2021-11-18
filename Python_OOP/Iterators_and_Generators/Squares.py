def squares(n):
    number = 1
    while number <= n:
        yield number * number
        number += 1

print(list(squares(5)))