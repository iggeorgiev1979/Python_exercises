cards = input().split(':')
command = input().split()
new_deck = []
while not command[0] == 'Ready':
    if command[0] == 'Add':
        if command[1] in cards:
            new_deck.append(command[1])
        else:
            print('Card not found.')
    elif command[0] == 'Insert':
        index = int(command[2])
        if 0 <= index < len(new_deck) and command[1] in cards:
            new_deck.insert(index, command[1])
        else:
            print('Error!')
    elif command[0] == 'Swap':
        index_1 = new_deck.index(command[1])
        index_2 = new_deck.index(command[2])
        new_deck[index_1], new_deck[index_2] = new_deck[index_2], new_deck[index_1]
    elif command[0] == 'Shuffle':
        new_deck.reverse()
    elif command[0] == 'Remove':
        if command[1] in new_deck:
            new_deck.remove(command[1])
        else:
            print('Card not found.')
    command = input().split()
print(*new_deck)
