def sum_numbers(numbers: list, n=0, result=0):
    if n < len(numbers):
        result += numbers[n]
        return sum_numbers(numbers, n + 1, result)
    return result


print(sum_numbers([-1, 0, 1]))
