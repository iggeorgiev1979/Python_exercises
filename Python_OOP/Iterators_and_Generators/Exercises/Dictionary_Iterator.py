class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = [el for el in self.dictionary.keys()]
        self.start = 0
        self.end = len(self.keys) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            key = self.keys[self.start]
            self.start += 1

            return key, self.dictionary[key]
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
