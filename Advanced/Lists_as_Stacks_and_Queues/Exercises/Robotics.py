import datetime
from collections import deque

robots = [x.split('-') for x in input().split(';')]
start_time = [int(x) for x in input().split(':')]
start_time = datetime.datetime(2021, 7, 1, start_time[0], start_time[1], start_time[2])
working = [0] * len(robots)
waiting = deque()
command = input()
put = True
while True:
    if command == 'End' and len(waiting) == 0:
        break
    start_time += datetime.timedelta(0, 1)
    if not command == 'End':
        waiting.appendleft(command)
    working = [n - 1 for n in working]
    for i in range(len(working)):
        if working[i] <= 0:
            put = True
            working[i] = int(robots[i][1])
            print(f'{robots[i][0]} - {waiting[0]} [{start_time.time()}]')
            waiting.popleft()
            break
        else:
            put = False
    if not put:
        waiting.append(waiting.popleft())

    if not command == 'End':
        command = input()

