from collections import deque

people = deque()
names = input()

while not names == 'End':
    if names == 'Paid':
        for _ in range(len(people)):
            print(people.popleft())
    else:
        people.append(names)

    names = input()

print(f'{len(people)} people remaining.')
