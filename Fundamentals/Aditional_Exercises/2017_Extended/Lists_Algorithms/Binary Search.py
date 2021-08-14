def binary(search, numbers):
    tmp = numbers.split()
    tmp.sort()
    low = 0
    high = len(tmp) - 1
    counter = 0
    result = None
    while not result:
        if high < low:
            break
        index = low + (high - low) // 2
        if search == int(tmp[index]):
            result = int(tmp[index])
        counter += 1
        if int(tmp[index]) < search:
            low = index + 1
        else:
            high = index - 1
    return counter


def linear(search, numbers):
    tmp = [int(x) for x in numbers.split()]
    counter = 0
    for i in tmp:
        counter += 1
        if i == search:
            break
    return counter


numbers_str = input()
number_for_search = int(input())
if str(number_for_search) in numbers_str.split():
    print('Yes')
else:
    print('No')
print(f'Linear search made {linear(number_for_search, numbers_str)} iterations')
print(f'Binary search made {binary(number_for_search, numbers_str)} iterations')