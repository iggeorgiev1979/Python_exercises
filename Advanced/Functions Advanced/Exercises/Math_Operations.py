def math_operations(*args, **kwargs):
    keys = {
        0: 'a',
        1: 's',
        2: 'd',
        3: 'm'
    }

    for el in range(len(args)):
        index = el % 4
        key = keys[index]
        value = args[el]

        if index == 0:
            kwargs[key] += value
        elif index == 1:
            kwargs[key] -= value
        elif index == 2:
            if not value == 0:
                kwargs[key] /= value
        elif index == 3:
            kwargs[key] *= value

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
