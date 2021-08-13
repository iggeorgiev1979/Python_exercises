number = int(input())
train = [x * 0 for x in range(number)]
command = input().split()
while not command[0] == 'End':
    if command[0] == 'add':
        train[number - 1] += int(command[1])
    elif command[0] == 'insert':
        train[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        train[int(command[1])] -= int(command[2])
    command = input().split()
print(train)
