numbers = list(map(lambda x: int(x), input().split()))
command = input().split()
while not command[0] == 'end':
    if command[0] == 'swap':
        numbers[int(command[1])], numbers[int(command[2])] = numbers[int(command[2])], numbers[int(command[1])]
    elif command[0] == 'multiply':
        result = numbers[int(command[1])] * numbers[int(command[2])]
        numbers[int(command[1])] = result
    elif command[0] == 'decrease':
        for i in range(len(numbers)):
            numbers[i] -= 1
    command = input().split()
print(*numbers, sep=', ')
