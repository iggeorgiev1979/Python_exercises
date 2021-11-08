class ExercisePlan:
    __id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.assign_id()

    @staticmethod
    def assign_id():
        tmp = ExercisePlan.__id
        ExercisePlan.__id += 1
        return tmp

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        return cls(trainer_id, equipment_id, hours * 60)

    @staticmethod
    def get_next_id():
        return ExercisePlan.__id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"


