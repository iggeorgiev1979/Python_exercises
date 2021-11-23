def cache(func):
    log = {}
    def wrapper(number):
        if number in log.keys():
            return log[number]
        log[number] = func(number)
        return log[number]
    
    wrapper.log = log
    
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(4)
print(fibonacci.log)
