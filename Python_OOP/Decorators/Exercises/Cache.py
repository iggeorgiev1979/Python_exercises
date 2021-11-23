def cache(func):
    pass



def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(4)
print(fibonacci.log)
