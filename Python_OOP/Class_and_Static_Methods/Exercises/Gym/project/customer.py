class Customer:
    __id = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.__assign_id()

    @staticmethod
    def __assign_id():
        tmp = Customer.__id
        Customer.__id += 1
        return tmp

    @staticmethod
    def get_next_id():
        return Customer.__id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


