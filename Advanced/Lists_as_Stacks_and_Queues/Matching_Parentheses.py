equation = input()
brackets = []
for index in range(len(equation)):
    if equation[index] == '(':
        brackets.append(index)
    elif equation[index] == ')':
        print(equation[brackets.pop():index + 1])
