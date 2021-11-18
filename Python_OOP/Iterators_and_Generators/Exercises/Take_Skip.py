class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.number = 0
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.count:
            tmp = self.number
            self.number += self.step
            self.start += 1
            return tmp
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
