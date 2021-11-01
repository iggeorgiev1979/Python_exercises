class Animal:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = None

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


