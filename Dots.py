n = int(input())
dots_list = []
result = 0
for _ in range(n):
    dots_list.append(list(input().split()))
for i in range(len(dots_list)):
    for j in range(len(dots_list[i])):
        if dots_list[i][j] == '.':
            initial_position = [i, j]
            position = initial_position
            previous_positions = []
            counter = 0
            while True:
                row = position[0]
                place = position[1]
                if dots_list[row][place] == '-':
                    break
                if not place == len(dots_list[row]) - 1 and dots_list[row][place + 1] == '.' and not [row, place + 1] in previous_positions:   # scan right
                    previous_positions.append([row, place])
                    position = [row, place + 1]
                elif not place == 0 and dots_list[row][place - 1] == '.' and not [row, place - 1] in previous_positions:   # scan left
                    previous_positions.append([row, place])
                    position = [row, place - 1]
                elif not row == 0 and dots_list[row - 1][place] == '.' and not [row - 1, place] in previous_positions:   # scan up
                    previous_positions.append([row, place])
                    position = [row - 1, place]
                elif not row == len(dots_list) - 1 and dots_list[row + 1][place] == '.' and not [row + 1, place] in previous_positions:   # scan down
                    previous_positions.append([row, place])
                    position = [row + 1, place]
                else:
                    dots_list[row][place] = '-'
                    counter += 1
                    position = initial_position
                    previous_positions = []
                if counter > result:
                    result = counter
print(result)


# 4
# - . - . - -
# . - . . - .
# . - - - - -
# - - - . - -