from collections import deque

available_food = int(input())
orders = deque(int(el) for el in input().split())
left_orders = []
print(max(orders))
for index in range(len(orders)):
    el = orders.popleft()
    if available_food - el >= 0:
        available_food -= el
    else:
        orders.appendleft(el)
        break


print('Orders complete') if len(orders) == 0 else print('Orders left: ', end='')
print(*orders)
