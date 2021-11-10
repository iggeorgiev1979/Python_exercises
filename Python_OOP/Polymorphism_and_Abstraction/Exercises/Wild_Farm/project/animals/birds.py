# from Polymorphism_and_Abstraction.Exercises.Wild_Farm.project.animals.animal import Bird


from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        food_type = type(food).__name__
        animal_type = type(self).__name__
        if food_type == "Meat":
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.25
        else:
            return f"{animal_type} does not eat {food_type}!"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.35
