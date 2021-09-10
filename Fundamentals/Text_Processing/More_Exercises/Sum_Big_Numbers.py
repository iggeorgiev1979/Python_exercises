def sum_big_number(number_1: str, number_2: str):
    result = ''
    if len(number_1) < len(number_2):
        x = len(number_2) - len(number_1)
        number_1 = '0' * x + number_1
    elif len(number_2) < len(number_1):
        x = len(number_1) - len(number_2)
        number_2 = '0' * x + number_2
    x = 0
    for el in range(len(number_1) - 1, -1, -1):
        sum_el = int(number_1[el]) + int(number_2[el]) + x
        result += str(sum_el % 10)
        x = sum_el // 10
    if not x == 0:
        result += str(x)
    result = result[::-1]
    # if result[0] == '0':
    #     result = result[1:]
    return result


el1 = input()
el2 = input()
final_result = sum_big_number(el1, el2)
print(final_result)
