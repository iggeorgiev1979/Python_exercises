import sys
sys.path.append(".")
from collections import deque
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.astronaut.meteorologist import Astronaut
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.completed_missions = 0
        self.uncompleted_missions = 0
        self.valid_types = {'Biologist': Biologist, 'Geodesist': Geodesist, 'Meteorologist': Meteorologist}

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.valid_types.keys():
            raise Exception("Astronaut type is not valid!")
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is not None:
            return f"{name} is already added."
        self.astronaut_repository.add(self.valid_types[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet is not None:
            return f"{name} is already added."
        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")
        suitable_astronauts = [astronaut for astronaut in self.astronaut_repository.astronauts if astronaut.oxygen > 30]
        if len(suitable_astronauts) < 1:
            raise Exception("You need at least one astronaut to explore the planet!")
        suitable_astronauts = sorted(suitable_astronauts, key=lambda x: x.oxygen, reverse=True)
        suitable_astronauts = deque(suitable_astronauts[:5])    
        participants = []
        while planet.items and suitable_astronauts:
            astronaut = suitable_astronauts[0]
            if astronaut.name not in participants:
                participants.append(astronaut.name)
            astronaut.backpack.append(planet.items.pop())
            astronaut.breathe()
            if astronaut.oxygen <= 0:
                suitable_astronauts.popleft()
        if len(planet.items) == 0:
            self.completed_missions += 1
            return f"Planet: {planet.name} was explored. {len(participants)} astronauts participated in collecting items."
        self.uncompleted_missions += 1
        return f"Mission is not completed."

    def report(self):
        out = [f"{self.completed_missions} successful missions!"]
        out.append(f"{self.uncompleted_missions} missions were not completed!")
        out.append("Astronauts' info:")
        for astronaut in self.astronaut_repository.astronauts:
            out.append(repr(astronaut))

        return '\n'.join(out)





# p = Planet("Earth")
# p.items = ["a", "b", "c", "d", "e", "f"]

# s = SpaceStation()
# print(s.add_planet("Mars", "a, b, c, d, e, f, g, h"))


# print(s.add_astronaut("Geodesist", "Eva"))

# s.planet_repository.add(p)

# print(s.send_on_mission("Earth"))

# print(s.report())



