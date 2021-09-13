size = int(input())
list_of_commands = input().split()
matrix = [[x for x in input().split()] for _ in range(size)]
start_position = [[i, j] for i in range(size) for j in range(size) if matrix[i][j] == 's']
total_coals = [1 for i in range(size) for j in range(size) if matrix[i][j] == 'c']
total_coals = len(total_coals)
collected_coals = 0
start = start_position[0]
boolean = True
for command in list_of_commands:
    if command == 'up':
        if not start[0] == 0:
            start = [start[0] - 1, start[1]]
    elif command == 'right':
        if not start[1] > size - 2:
            start = [start[0], start[1] + 1]
    elif command == 'left':
        if not start[1] == 0:
            start = [start[0], start[1] - 1]
    elif command == 'down':
        if not start[0] > size - 2:
            start = [start[0] + 1, start[1]]
    if matrix[start[0]][start[1]] == 'c':
        collected_coals += 1
        matrix[start[0]][start[1]] = '*'
        if collected_coals == total_coals:
            print(f'You collected all coal! ({start[0]}, {start[1]})')
            boolean = False
            break
    elif matrix[start[0]][start[1]] == 'e':
        print(f'Game over! ({start[0]}, {start[1]})')
        boolean = False
        break
if boolean:
    print(f'{total_coals - collected_coals} pieces of coal left. ({start[0]}, {start[1]})')
