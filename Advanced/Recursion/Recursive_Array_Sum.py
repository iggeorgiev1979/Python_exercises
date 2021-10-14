def sum_numbers(numbers: list, n=0):
    if n < len(numbers):
        return numbers[n] + sum_numbers(numbers, n + 1)
    return 0


print(sum_numbers([1, 2, 3, 4]))
