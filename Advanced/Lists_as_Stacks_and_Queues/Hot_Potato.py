names = input().split()
moves = int(input())
index = 0
while not len(names) == 1:
    index = (index + moves) % len(names) - 1
    if index == -1:
        index = len(names) - 1
    print(f'Removed {names[index]}')
    names.pop(index)
print(f'Last is {names[0]}')