from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]
wasted_water = 0
while True:
    if bottles[-1] >= cups[0]:
        wasted_water += bottles[-1] - cups[0]
        bottles.pop()
        cups.popleft()
    else:
        cups[0] -= bottles[-1]
        bottles.pop()
    if len(cups) == 0 or len(bottles) == 0:
        break
cups = [str(x) for x in cups]
bottles = [str(x) for x in bottles]
print(f'Bottles: {" ".join(bottles)}') if len(cups) == 0 else print(f'Cups: {" ".join(cups)}')
print(f'Wasted litters of water: {wasted_water}')
