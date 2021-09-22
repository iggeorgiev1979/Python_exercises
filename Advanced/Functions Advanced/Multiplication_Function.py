def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(multiply(1, 4, 5))