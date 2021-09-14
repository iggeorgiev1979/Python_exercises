from collections import deque

chocolate = [int(el) for el in input().split(', ')]
milk = deque(int(el) for el in input().split(', '))
counter = 0

while len(milk) > 0 and len(chocolate) > 0:
    choco_cup = chocolate.pop()
    milk_cup = milk.popleft()

    if choco_cup <= 0 or milk_cup <= 0:
        if choco_cup > 0:
            chocolate.append(choco_cup)
        if milk_cup > 0:
            milk.appendleft(milk_cup)
    elif choco_cup == milk_cup:
        counter += 1
    else:
        milk.append(milk_cup)
        chocolate.append(choco_cup - 5)

    if counter == 5:
        print("Great! You made all the chocolate milkshakes needed!")
        break
if counter < 5:
    print("Not enough milkshakes.")
if len(chocolate) > 0:
    print(f'Chocolate: {", ".join([str(el) for el in chocolate])}')
else:
    print("Chocolate: empty")
if len(milk) > 0:
    print(f'Milk: {", ".join([str(el) for el in milk])}')
else:
    print('Milk: empty')
