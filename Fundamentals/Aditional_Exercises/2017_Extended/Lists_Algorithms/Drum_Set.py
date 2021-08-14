money_available = float(input())
drums_str = input()
drums = [int(x) for x in drums_str.split()]
initial_values = [int(x) for x in drums_str.split()]
prices = [x * 3 for x in drums]
command = input()
while not command == 'Hit it again, Gabsy!':
    drums = [x - int(command) for x in drums]
    for i in range(len(drums)):
        if drums[i] <= 0:
            if money_available - prices[i] >= 0:
                drums[i] = initial_values[i]
                money_available -= prices[i]
    command = input()
drums = list(filter(lambda x: x > 0, drums))
print(*drums, sep=' ')
print(f'Gabsy has {money_available:.2f}lv.')
