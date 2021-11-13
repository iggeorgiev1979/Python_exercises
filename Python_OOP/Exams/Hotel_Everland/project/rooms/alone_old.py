from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, name: str, pension: float):
        super().__init__(name, pension, 1)
        self.room_cost = 10
        self.appliances = []
