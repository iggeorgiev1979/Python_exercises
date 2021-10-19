def factorial(number: int):
    if number == 0:
        return 1
    return number * factorial(number - 1)


print(factorial(5))
