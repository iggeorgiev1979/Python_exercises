from sys import maxsize

class CustomList:
    def __init__(self):
        self.__store = []
    
    def __validate_index(self, index):
        if index < 0 or index >= len(self.__store):
            raise IndexError(f"The index must be between 0 and {len(self.__store) - 1}")
    
    def append(self, value):
        self.__store.append(value)
        return self.__store

    def remove(self, index):
        self.__validate_index(index)

        return self.__store.pop(index)

    def get(self, index):
        self.__validate_index(index)
        return self.__store[index]

    def extend(self, value):
        if not hasattr(value, '__iter__'):
            raise Exception("The value is not iterable!")
        for el in value:
            self.__store.append(el)
        return self.__store

    def insert(self, index, value):
        self.__store.insert(index, value)
        return self.__store

    def pop(self):
        return self.__store.pop()

    def clear(self):
        self.__store = []

    def index(self, value):
        for index in range(len(self.__store)):
            if self.__store[index] == value:
                return index
        return f"({value}) is not in the list"

    def count(self, value):
        counter = 0
        for el in self.__store:
            if el == value:
                counter += 1
        return f"({value}) is contained {counter} times in the list."

    def reverse(self):
        result = []
        for index in range(len(self.__store) - 1, - 1, - 1):
            result.append(str(self.__store[index]))
        return ", ".join(result)

    def copy(self):
        return self.__store.copy()

    def size(self):
        return len(self.__store)
    
    def add_first(self, value):
        self.__store.insert(0, value)
        return self.__store

    def dictionize(self):
        result = {}
        for index in range(0, len(self.__store), 2):
            key = self.__store[index]
            value = self.__store[index + 1] if index < len(self.__store) - 1 else " "
            result[key] = value
        return result

    def move(self, amount):
        tmp = self.__store[:amount]
        self.__store = self.__store[3 - 1:]
        self.__store.extend(tmp)
        return self.__store

    def sum(self):
        sum_of_the_list = 0
        for el in self.__store:
            sum_of_the_list += el if type(el) == int or type(el) == float else len(el)
        return sum_of_the_list

    def overbound(self):
        max_value = -maxsize
        for el in self.__store:
            value = el if type(el) == float or type(el) == int else len(el)
            if value > max_value:
                max_value = value
        return max_value

    def underbound(self):
        min_value = maxsize
        for el in self.__store:
            value = el if type(el) == float or type(el) == int else len(el)
            if value < min_value:
                min_value = value
        return min_value

    def __repr__(self):
        return f"{', '.join(str(el) for el in self.__store)}"

ll = CustomList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5.2)
ll.append("abcsafsetjrsth")
print(ll.underbound())