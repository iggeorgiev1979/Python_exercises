numbers = input().split()
command = input()
while not command == 'end':
    numbers.insert(int(command[0]), command)
    command = input()
print(*numbers, sep=' ')
