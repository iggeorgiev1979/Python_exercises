import sys
from collections import deque
from io import StringIO

# input_1 = '''4, 6, 8, 5, 1
# 1, 9, 15, 10, 6'''
#
# input_2 = '''10, 5, 8, 9
# 2, 4, 5, 8'''
#
# input_3 = """2, 8, 4, 3, 11, 7
# 10, 15, 4, 6, 3, 10, 2, 1"""
#
# sys.stdin = StringIO(input_2)


def drive(people: deque, taxis: list):
    customer = people.popleft()
    car = taxis.pop()
    if car < customer:
        people.appendleft(customer)


customers = deque(int(el) for el in input().split(", "))
cars = [int(el) for el in input().split(", ")]
total_time = sum(customers)
while len(customers) > 0 and len(cars) > 0:
    drive(customers, cars)
if len(customers) == 0:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print("Customers left: ", end='')
    print(*customers, sep=", ")
