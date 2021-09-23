def even_odd(*args):
    args = list(args)
    command = args.pop()
    if command == "even":
        return list(filter(lambda x: x % 2 == 0, args))
    return list(filter(lambda x: x % 2 != 0, args))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))