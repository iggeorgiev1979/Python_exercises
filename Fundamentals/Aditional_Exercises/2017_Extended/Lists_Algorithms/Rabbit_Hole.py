def calculate(left_right, index_value, steps, len_list):
    if left_right == 'Left':
        if index_value + steps > len_list - 1:
            return (index_value + steps) % len_list
        return index_value + steps
    else:
        if index_value - steps < 0:
            return (index_value - steps) % len_list
        return index_value - steps


list_of_positions = input().split()
energy = int(input())
index = 0
while True:
    if list_of_positions[index] == 'RabbitHole':
        print("You have 5 years to save Kennedy!")
        break
    else:
        command = list_of_positions[index].split('|')
        if command[0] == 'Bomb':
            energy -= int(command[1])
            if energy <= 0:
                print('You are dead due to bomb explosion!')
                break
        else:
            index = calculate(command[0], index, int(command[1]), len(list_of_positions))
            energy -= int(command[1])
            if energy <= 0:
                print('You are tired. You can\'t continue the mission.')
                break
    list_of_positions.pop(-1)
    list_of_positions.append(f'Bomb|{energy}')



