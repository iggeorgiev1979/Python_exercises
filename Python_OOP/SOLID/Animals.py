class Animal:
    make_sound = ""

    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


class Dog(Animal):
    make_sound = "woof-woof"


class Cat(Animal):
    make_sound = "meow"


class Chicken(Animal):
    make_sound = "chick-chick"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound)


animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
