from project.appliances.appliance import Appliance


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.members_count = members_count
        self.budget = budget
        self.family_name = name
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for element in args:
            for el in element:
                if isinstance(el, Appliance):
                    result += el.get_monthly_expense()
                else:
                    result += el.cost * 30
        self.expenses = result



