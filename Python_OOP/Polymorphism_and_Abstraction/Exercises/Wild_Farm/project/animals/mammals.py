# from Polymorphism_and_Abstraction.Exercises.Wild_Farm.project.animals.animal import Mammal
from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        food_type = type(food).__name__
        animal_type = type(self).__name__
        if food_type == "Vegetable" or food_type == "Fruit":
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.1
        else:
            return f"{animal_type} does not eat {food_type}!"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        food_type = type(food).__name__
        animal_type = type(self).__name__
        if food_type == "Meat":
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.4
        else:
            return f"{animal_type} does not eat {food_type}!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        food_type = type(food).__name__
        animal_type = type(self).__name__
        if food_type == "Meat" or food_type == "Vegetable":
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.3
        else:
            return f"{animal_type} does not eat {food_type}!"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        food_type = type(food).__name__
        animal_type = type(self).__name__
        if food_type == "Meat":
            self.food_eaten += food.quantity
            self.weight += food.quantity * 1
        else:
            return f"{animal_type} does not eat {food_type}!"
