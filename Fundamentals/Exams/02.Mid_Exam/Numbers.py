numbers = list(map(lambda x: int(x), input().split()))
average_number = sum(numbers) / len(numbers)
numbers = list(sorted(filter(lambda x: x > average_number, numbers), reverse=True))
if len(numbers) == 0:
    print('No')
else:
    print(*numbers, sep=' ') if len(numbers) <= 5 else print(*numbers[:5], sep=' ')
