# from Polymorphism_and_Abstraction.Exercises.Animals.project.animal import Animal
from project.animal import Animal


class Cat(Animal):
    def make_sound(self):
        return "Meow meow!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"
