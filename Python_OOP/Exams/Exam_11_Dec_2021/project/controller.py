from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    _VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        cars = [el for el in self.cars if el.model == model]
        if cars:
            raise Exception(f"Car {model} is already created!")

        if car_type in self._VALID_CAR_TYPES.keys():
            car = self._VALID_CAR_TYPES[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        dr = [el for el in self.drivers if el.name == driver_name]
        if dr:
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        rc = [el for el in self.races if el.name == race_name]
        if rc:
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        try:
            driver = [el for el in self.drivers if el.name == driver_name][0]
        except IndexError:
            raise Exception(f"Driver {driver_name} could not be found!")

        available_cars = [el for el in self.cars if type(el).__name__ == car_type and not el.is_taken]
        if not available_cars:
            raise Exception(f"Car {car_type} could not be found!")
        car = available_cars.pop()
        if not driver.car:
            car.is_taken = True
            driver.car = car
            return f"Driver {driver_name} chose the car {car.model}."
        else:
            old_model = driver.car.model
            driver.car.is_taken = False
            car.is_taken = True
            driver.car = car
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        try:
            race = [el for el in self.races if el.name == race_name][0]
        except IndexError:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = [el for el in self.drivers if el.name == driver_name][0]
        except IndexError:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        try:
            race = [el for el in self.races if el.name == race_name][0]
        except IndexError:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_drivers = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)
        driver_one = fastest_drivers[0]
        driver_two = fastest_drivers[1]
        driver_tree = fastest_drivers[2]
        driver_one.number_of_wins += 1
        driver_two.number_of_wins += 1
        driver_tree.number_of_wins += 1

        return f"""Driver {driver_one.name} wins the {race_name} race with a speed of {driver_one.car.speed_limit}.
Driver {driver_two.name} wins the {race_name} race with a speed of {driver_two.car.speed_limit}.
Driver {driver_tree.name} wins the {race_name} race with a speed of {driver_tree.car.speed_limit}."""


# controller = Controller()
# print(controller.create_driver("Peter"))
# print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("SportsCar", "Porsche 911", 580))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
# print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
# print(controller.create_driver("John"))
# print(controller.create_driver("Jack"))
# print(controller.create_driver("Kelly"))
# print(controller.add_car_to_driver("Kelly", "MuscleCar"))
# print(controller.add_car_to_driver("Jack", "MuscleCar"))
# print(controller.add_car_to_driver("John", "SportsCar"))
# print(controller.create_race("Christmas Top Racers"))
# print(controller.add_driver_to_race("Christmas Top Racers", "John"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
# print(controller.start_race("Christmas Top Racers"))
# [print(d.name, d.number_of_wins) for d in controller.drivers]



