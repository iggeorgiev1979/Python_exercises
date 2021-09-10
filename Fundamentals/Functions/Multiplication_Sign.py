def multiplication(a, b, c):
    multiplication_list = [a, b, c]
    negative_counter = 0
    for i in multiplication_list:
        if i == 0:
            return 'zero'
        elif i < 0:
            negative_counter += 1
    if negative_counter % 2 == 0:
        return 'positive'
    else:
        return 'negative'


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(multiplication(num_1, num_2, num_3))
