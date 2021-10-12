from collections import deque


def best_list_pureness(chain: list, rotations: int):
    chain = deque(chain)

    def find_pureness(numbers: deque):
        pure = 0
        for position in range(len(numbers)):
            pure += numbers[position] * position
        return pure

    pureness = find_pureness(chain)
    index = 0
    for el in range(rotations):
        chain.appendleft(chain.pop())
        tmp = find_pureness(chain)
        if tmp > pureness:
            pureness = tmp
            index = el + 1
    return f"Best pureness {pureness} after {index} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
