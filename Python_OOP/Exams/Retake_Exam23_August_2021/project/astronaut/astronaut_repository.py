class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        searched_astronaut = [astronaut for astronaut in self.astronauts if astronaut.name == name]
        if searched_astronaut:
            return searched_astronaut[0]
