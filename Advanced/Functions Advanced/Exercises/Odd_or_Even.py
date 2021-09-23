def odd_sum(num: list, count: int):
    filtered_nums = list(filter(lambda x: x % 2 != 0, [int(el) for el in num]))
    return sum(filtered_nums) * count


def even_sum(num: list, count: int):
    filtered_nums = list(filter(lambda x: x % 2 == 0, [int(el) for el in num]))
    return sum(filtered_nums) * count


command = input()
numbers = input().split()

if command == "Odd":
    print(odd_sum(numbers, len(numbers)))
else:
    print(even_sum(numbers, len(numbers)))

