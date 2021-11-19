from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not value >= 51 and not value <= 100:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value

    # @property
    # def capacity(self):
    #     return self.__capacity
    #
    # @capacity.setter
    # def capacity(self, value):
    #     if value <= 0:
    #         raise ValueError("Capacity has to be greater than 0!")
    #     self.__capacity = value
