from collections import deque

green_duration = int(input())
window = int(input())
command = input()
green = 0
cars_passed = 0
waiting_cars = deque()
crash = False
passing = False
while not command == 'END':
    if not green == 0 and not len(waiting_cars) == 0:
        passing = True
        green -= len(waiting_cars[0])
        if green >= 0:
            cars_passed += 1
            waiting_cars.popleft()
            if len(waiting_cars) == 0 or green == 0:
                green = 0
                passing = False
        else:
            green += window
            if green < 0:
                print(f'A crash happened!\n{waiting_cars[0]} was hit at {waiting_cars[0][green]}.')
                crash = True
                break
            else:
                green = 0
                cars_passed += 1
                waiting_cars.clear()
                passing = False
    else:
        if not command == 'green':
            waiting_cars.append(command)
    if not passing:
        command = input()
        if command == 'green':
            green = green_duration
if not crash:
    print(f'Everyone is safe.\n{cars_passed} total cars passed the crossroads.')
