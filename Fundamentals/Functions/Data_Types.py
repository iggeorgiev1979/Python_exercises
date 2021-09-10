def integer(a):
    return int(a) * 2


def floating(a):
    return f'{float(a) * 1.5:.2f}'


def string(a):
    return f'${a}$'


input_type = input()
input_line = input()
if input_type == 'int':
    result = integer(input_line)
elif input_type == 'real':
    result = floating(input_line)
else:
    result = string(input_line)
print(result)