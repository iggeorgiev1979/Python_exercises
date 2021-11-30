from abc import ABC, abstractmethod


class Astronaut(ABC):

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == '' or value.isspace():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def __repr__(self):
        out = [f"Name: {self.name}"]
        out.append(f"Oxygen: {self.oxygen}")
        if self.backpack:
            out.append(f"Backpack items: {', '.join(self.backpack)}")
        else:
            out.append(f"Backpack items: none")
        return '\n'.join(out)
        
    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
