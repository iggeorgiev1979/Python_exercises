from abc import ABC, abstractmethod


class Astronaut(ABC):
    oxygen_decrease_value = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        striped_value = value.strip()
        if not striped_value:
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def __str__(self):
        if self.backpack:
            list_of_items = ", ".join(self.backpack)
        else:
            list_of_items = "none"
        return f"Name: {self.name}\n" \
               f"Oxygen: {self.oxygen}\n" \
               f"Backpack items: {list_of_items}"

    def breathe(self):
        self.oxygen -= self.oxygen_decrease_value

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
