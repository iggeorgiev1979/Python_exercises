houses = list(map(lambda x: int(x), input().split('@')))
command = input().split()
index = 0
while not command[0] == 'Love!':
    jump = int(command[1])
    if index + jump < len(houses):
        index += jump
    else:
        index = 0
    if houses[index] == 0:
        print(f'Place {index} already had Valentine\'s day.')
    else:
        houses[index] -= 2
        if houses[index] == 0:
            print(f'Place {index} has Valentine\'s day.')
    command = input().split()
print(f'Cupid\'s last position was {index}.')
if sum(houses) == 0:
    print('Mission was successful.')
else:
    failed = [x for x in houses if not x == 0]
    print(f'Cupid has failed {len(failed)} places.')

