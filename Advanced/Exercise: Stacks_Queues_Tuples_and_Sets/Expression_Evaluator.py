from collections import deque


def add(numbers: deque):
    return sum(numbers)


def multiply(numbers: deque):
    result = 1
    for i in numbers:
        result *= i
    return result


def subtract(numbers: deque):
    result = numbers.popleft()
    for i in numbers:
        result -= i
    return result


def divide(numbers: deque):
    result = numbers.popleft()
    for i in numbers:
        result //= i
    return result


equation = deque(input().split())
tmp = deque()
while True:
    el = equation.popleft()
    if el == '*':
        equation.appendleft(multiply(tmp))
        tmp.clear()
    elif el == '+':
        equation.appendleft(add(tmp))
        tmp.clear()
    elif el == '-':
        equation.appendleft(subtract(tmp))
        tmp.clear()
    elif el == '/':
        equation.appendleft(divide(tmp))
        tmp.clear()
    else:
        tmp.append(int(el))
    if len(equation) == 1 and len(tmp) == 0:
        break

print(*equation)
