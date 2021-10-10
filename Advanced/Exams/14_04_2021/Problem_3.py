def flights(*args):
    register = {}
    for index in range(0, len(args) - 1, 2):
        destination = args[index]
        passengers = args[index + 1]
        if destination == "Finish":
            return register
        if destination not in register.keys():
            register[destination] = 0
        register[destination] += passengers
    return register


# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
