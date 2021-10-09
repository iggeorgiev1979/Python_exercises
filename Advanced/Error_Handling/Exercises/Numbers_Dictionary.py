numbers_dict = {}
line = input()

while not line == "Search":
    try:
        number = int(input())
        numbers_dict[line] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

line = input()

while not line == "Remove":
    try:
        print(numbers_dict[line])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

line = input()

while not line == "End":
    try:
        del numbers_dict[line]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dict)

