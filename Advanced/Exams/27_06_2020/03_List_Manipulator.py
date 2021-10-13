from collections import deque


def list_manipulator(numbers: list, command: str, position: str, *args):
    numbers = deque(numbers)
    if command == "add":
        if position == "beginning":
            numbers = add_at_the_beginning(numbers, args)
        elif position == "end":
            numbers = add_at_the_end(numbers, args)

    elif command == "remove":
        if position == "beginning":
            remove_from_the_beginning(numbers, args)
        elif position == "end":
            remove_from_the_end(numbers, args)

    return list(numbers)


def add_at_the_beginning(numbers: deque, new_numbers: tuple):
    numbers.extendleft(reversed(new_numbers))
    return numbers


def add_at_the_end(numbers: deque, new_numbers: tuple):
    numbers.extend(new_numbers)
    return numbers


def remove_from_the_beginning(numbers: deque, new_numbers: tuple):
    if len(new_numbers) == 0:
        numbers.popleft()
    else:
        for _ in range(new_numbers[0]):
            numbers.popleft()
    return numbers


def remove_from_the_end(numbers: deque, new_numbers: tuple):
    if len(new_numbers) == 0:
        numbers.pop()
    else:
        for _ in range(new_numbers[0]):
            numbers.pop()
    return numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
