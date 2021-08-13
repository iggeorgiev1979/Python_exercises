list_of_numbers = list(map(lambda x: int(x), input().split(', ')))
end = 10
while len(list_of_numbers) > 0:
    group = []
    for i in range(len(list_of_numbers) - 1, -1, -1):
        if list_of_numbers[i] <= end:
            number = list_of_numbers.pop(i)
            group.append(number)
    group.reverse()
    print(f'Group of {end}\'s: {group}')
    end += 10
