def numbers_searching(*args):
    missing_number = ''
    min_number = min(args)
    max_number = max(args)
    chain = set(args)
    for el in range(min_number, max_number + 1):
        if el not in chain:
            missing_number = el
            break
    repeating_numbers = set(filter(lambda x: args.count(x) > 1, args))
    return [missing_number, sorted(repeating_numbers)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
