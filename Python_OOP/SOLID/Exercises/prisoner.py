from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, position):
        self.position = position

    @abstractmethod
    def walk_north(self, dist):
        pass

    @abstractmethod
    def walk_east(self, dist):
        pass


class FreePerson(Person):

    def __init__(self, position):
        super().__init__(position)

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class LockedPerson(Person):
    def __init__(self, position):
        super().__init__(position)

    def walk_north(self, dist):
        pass

    def walk_east(self, dist):
        pass


class Prisoner(LockedPerson):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(self.PRISON_LOCATION.copy())
        self.is_free = False


class Citizen(FreePerson):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(self.PRISON_LOCATION.copy())
        self.is_free = False


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")
print()

free_person = Citizen()
print("The citizen trying to walk to north by 10 and east by -3.")

try:
    free_person.walk_north(10)
    free_person.walk_east(-3)
except:
    pass

print(f"The location of the prison: {free_person.PRISON_LOCATION}")
print(f"The current position of the citizen: {free_person.position}")
