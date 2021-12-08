class HashTable:
    def __init__(self):
        self.__len = 4
        self.__free_slots = self.__len
        self.__store = [None] * self.__len
    
    def __grow(self):
        self.__len *= 2
        self.__free_slots = self.__len
        self.__replace_elements()
        
    def __replace_elements(self):
        __new_store = self.__store.copy()
        self.__store = [None] * self.__len
        for cell in __new_store:
            if cell is not None:
                for element in cell:
                    key, value = element
                    self.add(key, value)

    def hash(self, key):
        return abs(hash(key)) % self.__len

    def add(self, key, value):
        index = self.hash(key)
        if self.__store[index] is None:
            self.__store[index] = []
            self.__free_slots -= 1
        
        for (k, v) in self.__store[index]:
            if k == key:
                self.__store[index].remove((k, v))
                break
        self.__store[index].append((key, value))

        if self.__free_slots < self.__len * 0.3:
            self.__grow()
    
    def get(self, key):
        index = self.hash(key)
        cell = self.__store[index]
        if cell is not None:
            for k, v in cell:
                if k == key:
                    return v
        print("The key is not found!")

    def __len__(self):
        len_of_the_table = 0
        for cell in self.__store:
            if cell is not None:
                for element in cell:
                    len_of_the_table += 1
        return len_of_the_table

    def __setitem__(self, key, value):
        self.add(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
    
    
    

    

my_dict = HashTable()
my_dict.add("Name", "Ivan")
my_dict.add("Age", 42)
my_dict.add("Height", 192)
my_dict.add("Weight", 105)
my_dict.add("Name", "George")
my_dict.add("Name1", "Ivan")
my_dict.add("Name2", "Ivo")
my_dict.add("Name3", "Ivailo")
my_dict.add("Name4", "Ivanchev")
my_dict.add("Name5", "Ivandrago")
my_dict["family"] = "Georgiev"
kk = my_dict.get("Name4")
print(kk)
cc = my_dict["family"]
print(cc)
print(len(my_dict))



