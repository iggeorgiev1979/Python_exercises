from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.completed_missions = 0
        self.uncompleted_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if not self.the_astronaut_type_is_valid(astronaut_type):
            raise Exception("Astronaut type is not valid!")
        else:
            new_astronaut = self.create_astronaut(astronaut_type, name)
            astronaut = self.astronaut_repository.find_by_name(name)
            if astronaut:
                return f"{name} is already added."
            self.astronaut_repository.add(new_astronaut)
            return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f"{name} is already added."
        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exists!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")
        suitable_astronauts = [astronaut for astronaut in self.astronaut_repository if astronaut.oxygen > 30]
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")
        suitable_astronauts = self.give_me_the_best_astronauts(suitable_astronauts)
        for astronaut in suitable_astronauts:
            while astronaut.oxygen > 0 and planet.items:
                # if astronaut.oxygen - astronaut.oxygen_decrease_value < 0:
                #     break
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
                if astronaut.oxygen < 0:
                    astronaut.oxygen = 0

            planet.counter += 1
            if not planet.items:
                self.completed_missions += 1
                self.planet_repository.remove(planet)
                return f"Planet: {planet_name} was explored. {planet.counter} astronauts participated in collecting items."
        self.uncompleted_missions += 1
        # planet.counter = 0
        return f"Mission is not completed."

    def report(self):
        astronauts_info = "\n".join([el.__str__() for el in self.astronaut_repository])
        return f"{self.completed_missions} successful missions!\n" \
               f"{self.uncompleted_missions} missions were not completed!\n" \
               f"Astronauts' info:\n" \
               f"{astronauts_info}"

    @staticmethod
    def the_astronaut_type_is_valid(checked_type: str):
        if checked_type == "Biologist" or checked_type == "Geodesist" or checked_type == "Meteorologist":
            return True
        return False

    @staticmethod
    def create_astronaut(type_name, object_name):
        if type_name == "Biologist":
            return Biologist(object_name)
        if type_name == "Geodesist":
            return Geodesist(object_name)
        if type_name == "Meteorologist":
            return Meteorologist(object_name)

    @staticmethod
    def give_me_the_best_astronauts(astronauts: list):
        astronauts.sort(key=lambda x: x.oxygen, reverse=True)
        if len(astronauts) <= 5:
            return astronauts
        return astronauts[:5]




# p = Planet("Earth")
# p.items = ["a", "b", "c", "d", "e", "f"]
#
# s = SpaceStation()
# print(s.add_planet("Mars", "a, b, c, d, e, f, g, h"))
#
#
# print(s.add_astronaut("Geodesist", "Eva"))
#
# s.planet_repository.add(p)
#
# print(s.send_on_mission("Earth"))
#
# print(s.report())



