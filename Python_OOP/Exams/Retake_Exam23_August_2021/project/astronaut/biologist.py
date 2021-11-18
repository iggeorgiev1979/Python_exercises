from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    oxygen_decrease_value = 5

    def __init__(self, name: str):
        super().__init__(name, 70)

