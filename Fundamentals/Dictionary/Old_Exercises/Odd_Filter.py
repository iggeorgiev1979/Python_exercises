numbers = list(filter(lambda x: x % 2 == 0, [int(y) for y in input().split()]))
average = sum(numbers) / len(numbers)
numbers = [x - 1 if x <= average else x + 1 for x in numbers]
print(*numbers)
