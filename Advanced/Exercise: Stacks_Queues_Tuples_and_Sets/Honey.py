from collections import deque


def add(first_el, second_el):
    return abs(first_el + second_el)


def subtract(first_el, second_el):
    return abs(first_el - second_el)


def multiply(first_el, second_el):
    return abs(first_el * second_el)


def divide(first_el, second_el):
    if second_el == 0:
        return 0
    return abs(first_el / second_el)


bees = deque(int(el) for el in input().split())
flowers = [int(el) for el in input().split()]
operands = deque(el for el in input().split())
working_bee = None
total_honey = 0

while len(bees) > 0 and len(flowers) > 0:
    working_bee = bees.popleft()
    honey = flowers.pop()

    if working_bee <= honey:
        command = operands.popleft()
        if command == '+':
            total_honey += add(working_bee, honey)
        elif command == '-':
            total_honey += subtract(working_bee, honey)
        elif command == '*':
            total_honey += multiply(working_bee, honey)
        elif command == '/':
            total_honey += divide(working_bee, honey)
    else:
        bees.appendleft(working_bee)


print(f"Total honey made: {total_honey}")
if len(bees) > 0:
    print('Bees left:', end=' ')
    print(*bees, sep=', ')
if len(flowers) > 0:
    print('Nectar left:', end=' ')
    print(*flowers, sep=', ')
