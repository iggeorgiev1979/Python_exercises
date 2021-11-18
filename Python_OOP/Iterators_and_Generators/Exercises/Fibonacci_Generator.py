def fibonacci():
    x = 0
    y = 1
    counter = 1
    while True:
        if counter == 1:
            yield x
        elif counter == 2:
            yield y
        yield x + y
        x, y = y, x + y
        counter += 1


generator = fibonacci()
for i in range(5):
    print(next(generator))
