from functools import wraps

def store_results(func):
    wraps(func)
    def wrapper(*args):
        file = open("results.txt", "a")
        file.write(f"Function {func.__name__} was add called. Result: {func(*args)}\n")
        file.close()
    return wrapper

@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)