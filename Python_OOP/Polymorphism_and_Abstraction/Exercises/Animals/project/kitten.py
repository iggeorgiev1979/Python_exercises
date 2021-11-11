# from Polymorphism_and_Abstraction.Exercises.Animals.project.cat import Cat
from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age, gender="Female"):
        super().__init__(name, age, gender)
        self.gender = "Female"

    def make_sound(self):
        return "Meow"
