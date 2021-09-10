def add_stop(route: str, action: list):
    index = int(action[1])
    new_stop = action[2]
    if 0 <= index < len(route):
        route = route[:index] + new_stop + route[index:]
    print(route)
    return route


def remove_stop(route: str, action: list):
    start = int(action[1])
    end = int(action[2])
    if 0 <= start < len(route) and start <= end < len(route):
        route = route[:start] + route[end + 1:]
    print(route)
    return route


def switch(route: str, action: list):
    old = action[1]
    new = action[2]
    if old in route:
        route = route.replace(old, new)
    print(route)
    return route


text = input()
command = input()
while not command == 'Travel':
    command = command.split(':')
    if command[0] == 'Add Stop':
        text = add_stop(text, command)
    elif command[0] == 'Remove Stop':
        text = remove_stop(text, command)
    elif command[0] == 'Switch':
        text = switch(text, command)
    command = input()
print(f"Ready for world tour! Planned stops: {text}")
