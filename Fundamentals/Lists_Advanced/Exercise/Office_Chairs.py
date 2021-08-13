n = int(input())
rooms = []
for _ in range(n):
    x = input().split()
    rooms.append(x)
free_chairs = 0
is_not_enough = False
for i in range(len(rooms)):
    if len(rooms[i][0]) >= int(rooms[i][1]):
        free_chairs += len(rooms[i][0]) - int(rooms[i][1])
    else:
        is_not_enough = True
        print(f'{int(rooms[i][1]) - len(rooms[i][0])} more chairs needed in room {i + 1}')
if not is_not_enough:
    print(f'Game On, {free_chairs} free chairs left')
