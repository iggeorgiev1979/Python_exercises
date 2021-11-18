class vowels:
    def __init__(self, some_str: str):
        self.some_str = some_str
        self.start = 0
        self.vowels = {"a", "e", "i", "o", "u", "y"}
        self.some_list = [el for el in self.some_str if el.lower() in self.vowels]
        self.end = len(self.some_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            index = self.start
            self.start += 1
            return self.some_list[index]
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

