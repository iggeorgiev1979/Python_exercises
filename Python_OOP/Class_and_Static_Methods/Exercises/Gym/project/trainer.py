class Trainer:
    __id = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer.assign_id()

    @staticmethod
    def assign_id():
        tmp = Trainer.__id
        Trainer.__id += 1
        return tmp

    @staticmethod
    def get_next_id():
        return Trainer.__id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

