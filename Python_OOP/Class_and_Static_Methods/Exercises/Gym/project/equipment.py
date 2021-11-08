class Equipment:
    __id = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.assign_id()

    @staticmethod
    def assign_id():
        tmp = Equipment.__id
        Equipment.__id += 1
        return tmp

    @staticmethod
    def get_next_id():
        return Equipment.__id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_net_id():
        return Equipment.__id


