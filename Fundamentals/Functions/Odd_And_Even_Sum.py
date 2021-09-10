number = input()


def odd_sum(a):
    result = 0
    for i in a:
        if not int(i) % 2 == 0:
            result += int(i)
    return result


def even_sum(a):
    result = 0
    for i in a:
        if int(i) % 2 == 0:
            result += int(i)
    return result


print(f'Odd sum = {odd_sum(number)}, Even sum = {even_sum(number)}')
