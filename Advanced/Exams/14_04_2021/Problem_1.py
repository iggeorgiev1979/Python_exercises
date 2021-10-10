pizzas = [x for x in input().split(', ') if 0 < int(x) <= 10]
employees = input().split(', ')
pizza_counter = 0
while True:
    if len(pizzas) == 0 or len(employees) == 0:
        break
    if int(pizzas[0]) <= int(employees[-1]):
        pizza_counter += int(pizzas[0])
        pizzas.pop(0)
        employees.pop()
    else:
        pizza_counter += int(employees[-1])
        pizzas[0] = str(int(pizzas[0]) - int(employees[-1]))
        employees.pop()

if len(pizzas) == 0:
    print(
        f"All orders are successfully completed!\nTotal pizzas made: {pizza_counter}\nEmployees: {', '.join(employees)}")
else:
    print(f"Not all orders are completed.\nOrders left: {', '.join(pizzas)}")
