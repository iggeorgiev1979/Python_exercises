from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    oxygen_decrease_value = 10

    def __init__(self, name: str):
        super().__init__(name, 50)

    def breathe(self):
        self.oxygen -= 10