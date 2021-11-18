class reverse_iter:
    def __init__(self, my_list):
        self.my_list = my_list
        self.end = 0
        self.start = len(my_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            i = self.start
            self.start -= 1
            return self.my_list[i]
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)


