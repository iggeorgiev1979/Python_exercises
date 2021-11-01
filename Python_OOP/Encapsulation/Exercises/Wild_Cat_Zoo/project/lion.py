from project.animal import Animal


class Lion(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age)
        self.money_for_care = 50
