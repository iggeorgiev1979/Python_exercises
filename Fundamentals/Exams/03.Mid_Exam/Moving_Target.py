targets = list(map(lambda x: int(x), input().split()))
command = input().split()
while not command[0] == 'End':
    if command[0] == 'Shoot':
        index = int(command[1])
        if 0 <= index < len(targets):
            targets[index] -= int(command[2])
        if targets[index] <= 0:
            targets.pop(index)
    elif command[0] == 'Add':
        index = int(command[1])
        targets.insert(index, int(command[2])) if 0 <= index < len(targets) else print('Invalid placement!')
    elif command[0] == 'Strike':
        index = int(command[1])
        radius = int(command[2])
        if index - radius >= 0 and index + radius < len(targets):
            del targets[index - radius: index + radius + 1]
        else:
            print('Strike missed!')
    command = input().split()
print(*targets, sep='|')
