loot = input().split('|')
command = input().split()
while not command[0] == 'Yohoho!':
    if command[0] == 'Loot':
        for new_loot in command[1:]:
            if new_loot not in loot:
                loot.insert(0, new_loot)
    elif command[0] == 'Drop':
        try:
            dropped_item = loot.pop(int(command[1]))
            loot.append(dropped_item)
        except:
            pass
    elif command[0] == 'Steal':
        if int(command[1]) >= len(loot):
            print(', '.join(loot))
            loot = []
        else:
            stolen_items = loot[-int(command[1]):]
            del loot[-int(command[1]):]
            print(', '.join(stolen_items))
    command = input().split()
if len(loot) == 0:
    print('Failed treasure hunt.')
else:
    average = 0
    for i in loot:
        average += len(i)
    average /= len(loot)
    print(f'Average treasure gain: {average:.2f} pirate credits.')
