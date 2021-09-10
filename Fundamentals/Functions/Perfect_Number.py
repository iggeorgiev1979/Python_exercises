number = int(input())


def perfect_number(c):
    a = 0
    b = []
    for i in range(1, c):
        if number % i == 0:
            b.append(i)
    if sum(b) == c:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


perfect_number(number)
