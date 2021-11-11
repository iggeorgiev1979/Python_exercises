# from Polymorphism_and_Abstraction.Exercises.Animals.project.cat import Cat
from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age, gender="Male"):
        super().__init__(name, age, gender)
        self.gender = "Male"

    def make_sound(self):
        return "Hiss"

