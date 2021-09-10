numbers = input().split()
command = input().split()
moves = 0
is_valid = True
while not command[0] == 'end':
    moves += 1
    if 0 <= int(command[0]) < len(numbers) and 0 <= int(command[1]) < len(numbers) and not command[0] == command[1]:
        is_valid = True
    else:
        is_valid = False
        print('Invalid input! Adding additional elements to the board')
        numbers.insert(len(numbers) // 2, '-' + str(moves) + 'a')
        numbers.insert(len(numbers) // 2, '-' + str(moves) + 'a')
    if is_valid:
        if not numbers[int(command[0])] == numbers[int(command[1])]:
            print('Try again!')
        else:
            print(f'Congrats! You have found matching elements - {numbers[int(command[1])]}!')
            a = numbers[int(command[0])]
            numbers.remove(a)
            numbers.remove(a)
    if len(numbers) == 0:
        print(f'You have won in {moves} turns!')
        break
    command = input().split()
if len(numbers) > 0:
    print(f'Sorry you lose :(\n{" ".join(numbers)}')
