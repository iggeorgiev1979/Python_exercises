class Subscription:
    __id = 1

    def __init__(self, date: str, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.assign_id()

    @staticmethod
    def assign_id():
        tmp = Subscription.__id
        Subscription.__id += 1
        return tmp

    @staticmethod
    def get_next_id():
        return Subscription.__id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

