neighbourhood = list(map(lambda x: int(x), input().split('@')))
command = input().split()
start_position = 0
while not command[0] == 'Love!':
    jump = int(command[1])
    if start_position + jump < len(neighbourhood):
        start_position += jump
    else:
        start_position = 0

    if neighbourhood[start_position] == 0:
        print(f'Place {start_position} already had Valentine\'s day.')
    else:
        neighbourhood[start_position] -= 2
        if neighbourhood[start_position] == 0:
            print(f'Place {start_position} has Valentine\'s day.')
    command = input().split()
print(f'Cupid\'s last position was {start_position}.')
if sum(neighbourhood) == 0:
    print('Mission was successful.')
else:
    neighbourhood = list(filter(lambda x: not x == 0, neighbourhood))
    print(f'Cupid has failed {len(neighbourhood)} places.')
