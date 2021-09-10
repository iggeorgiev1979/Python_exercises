friends = input().split(', ')
command = input().split()
lost = 0
black = 0
while not command[0] == 'Report':
    if command[0] == 'Blacklist':
        if command[1] in friends:
            index = friends.index(command[1])
            friends[index] = 'Blacklisted'
            print(f'{command[1]} was blacklisted.')
            black += 1
        else:
            print(f'{command[1]} was not found.')
    elif command[0] == 'Error':
        index = int(command[1])
        if 0 <= index < len(friends):
            if not friends[index] == 'Blacklisted' and not friends[index] == 'Lost':
                print(f'{friends[index]} was lost due to an error.')
                friends[index] = 'Lost'
                lost += 1
    elif command[0] == 'Change':
        index = int(command[1])
        if 0 <= index < len(friends):
            print(f'{friends[index]} changed his username to {command[2]}.')
            friends[index] = command[2]
    command = input().split()
print(f'Blacklisted names: {black}')
print(f'Lost names: {lost}')
print(*friends)
