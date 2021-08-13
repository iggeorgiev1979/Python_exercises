n = int(input())
maze = []
for _ in range(n):
    maze.append(list(input()))
initial_position = []
for row in range(len(maze)):  # finding the initial position of Kate
    for place in range(len(maze[row])):
        if maze[row][place] == 'k':
            initial_position = [row, place]
            break
    if len(initial_position) == 2:
        break
position = initial_position
previous_positions = []
while True:
    row = position[0]
    place = position[1]
    if maze[row][place] == '#':
        print('Kate cannot get out')
        break
    if maze[row][place + 1] == ' ' and not [row, place + 1] in previous_positions:  # scan left
        position = [row, place + 1]
        previous_positions.append([row, place])
    elif maze[row][place - 1] == ' ' and not [row, place - 1] in previous_positions:  # scan right
        position = [row, place - 1]
        previous_positions.append([row, place])
    elif maze[row - 1][place] == ' ' and not [row - 1, place] in previous_positions:  # scan up
        position = [row - 1, place]
        previous_positions.append([row, place])
    elif maze[row + 1][place] == ' ' and not [row + 1, place] in previous_positions:  # scan down
        position = [row + 1, place]
        previous_positions.append([row, place])
    else:
        maze[row][place] = '#'
        previous_positions = []
        position = initial_position

    if position[0] == len(maze) - 1 or position[0] == 0 or position[1] == 0 or position[1] == len(maze[row]) - 1:
        print(f'Kate got out in {len(previous_positions) + 1} moves')
        break
