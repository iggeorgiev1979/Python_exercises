char_1 = input()
char_2 = input()


def print_range(a, b):
    result = ''
    for i in range(ord(a) + 1, ord(b)):
        result += chr(i) + ' '
    return result


print(print_range(char_1, char_2))
