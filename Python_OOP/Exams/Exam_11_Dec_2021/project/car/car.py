from abc import ABC, abstractmethod


class Car(ABC):
    _MIN_SPEED = 0
    _MAX_SPEED = 0

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not value >= self._MIN_SPEED or not value <= self._MAX_SPEED:
            raise ValueError(f"Invalid speed limit! Must be between {self._MIN_SPEED} and {self._MAX_SPEED}!")
        self.__speed_limit = value
