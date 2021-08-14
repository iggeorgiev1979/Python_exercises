def calculate(index_value, power, direction):
    if direction == 'Left':
        if index_value + power > 5:
            return (index_value + power) % 6
        return index_value + power
    else:
        if index_value - power < 0:
            return (index_value - power) % 6
        return index_value - power


pistol = input().split()
command = input().split()
boolean = True
index = 2
for i in range(len(command)):
    rotation = command[i].split(',')
    index = calculate(index, int(rotation[0]), rotation[1])
    if pistol[index] == '1':
        boolean = False
        print(f'Game over! Player {i} is dead.')
        break
    index -= 1
    if index < 0:
        index = 5
if boolean:
    print('Everybody got lucky!')
