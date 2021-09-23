def operate(operator: str, *operands):
    if operator == "+":
        return sum(operands)
    elif operator == "*":
        result = 1
        for el in operands:
            result *= el
        return result
    elif operator == "-":
        result = operands[0]
        for el in range(1, len(operands)):
            result -= operands[el]
        return result
    elif operator == "/":
        result = operands[0]
        for el in range(1, len(operands)):
            result /= operands[el]
        return result


print(operate("-", 1, 2, 3))
