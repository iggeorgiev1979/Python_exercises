class Zoo:
    animals = 0

    def __init__(self, name):
        self.name = name
        self.mammal = []
        self.fish = []
        self.bird = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammal.append(name)
        elif species == 'fish':
            self.fish.append(name)
        elif species == 'bird':
            self.bird.append(name)

    def get_info(self, species):
        if species == 'mammal':
            return f'Mammals in {self.name}: {", ".join(self.mammal)}\nTotal animals: {self.animals}'
        elif species == 'fish':
            return f'Fishes in {self.name}: {", ".join(self.fish)}\nTotal animals: {self.animals}'
        elif species == 'bird':
            return f'Birds in {self.name}: {", ".join(self.bird)}\nTotal animals: {self.animals}'


zoo_name = input()
zoo_object = Zoo(zoo_name)
n = int(input())
for _ in range(n):
    txt = input().split()
    zoo_object.add_animal(txt[0], txt[1])
    zoo_object.animals += 1
command = input()
print(zoo_object.get_info(command))
