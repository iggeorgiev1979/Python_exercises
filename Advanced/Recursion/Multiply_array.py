def multiply(numbers: list, index=0):
    if index == len(numbers):
        return 1
    return numbers[index] * multiply(numbers, index + 1)


print(multiply([1, 2, 3, 4]))

