class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.number = number
        self.sequence = sequence
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.number:
            index = self.start % len(self.sequence)
            self.start += 1
            return self.sequence[index]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
