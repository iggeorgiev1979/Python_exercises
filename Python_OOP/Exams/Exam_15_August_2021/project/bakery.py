from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        tmp = value.strip()
        if not tmp:
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @staticmethod
    def create_food(food_type, food_name, price):
        if food_type == "Bread":
            return Cake(food_name, price)
        elif food_type == "Cake":
            return Bread(food_name, price)

    @staticmethod
    def create_drink(drink_type, name, portion, brand):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        elif drink_type == "Water":
            return Water(name, portion, brand)

    @staticmethod
    def create_table(table_type, table_number, capacity):
        if table_type == "InsideTable":
            return InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            return OutsideTable(table_number, capacity)

    @staticmethod
    def search_by_number(number, repository):
        tmp = [el for el in repository if el.table_number == number]
        if tmp:
            return True
        return False

    @staticmethod
    def search_by_name(name, repository):
        tmp = [el for el in repository if el.name == name]
        if tmp:
            return True
        return False

    def add_food(self, food_type: str, name: str, price: float):
        new_food = self.create_food(food_type, name, price)
        if new_food:
            name_exists = self.search_by_name(name, self.food_menu)
            if name_exists:
                raise Exception(f"{food_type} {name} is already in the menu!")
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        new_drink = self.create_drink(drink_type, name, portion, brand)
        if new_drink:
            name_exists = self.search_by_name(name, self.drinks_menu)
            if name_exists:
                raise Exception(f"{drink_type} {name} is already in the menu!")
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        new_table = self.create_table(table_type, table_number, capacity)
        if new_table:
            number_exists = self.search_by_number(table_number, self.tables_repository)
            if number_exists:
                raise Exception(f"Table {table_number} is already in the bakery!")
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *args):
        try:
            table = [table for table in self.tables_repository if table.table_number == table_number][0]
            unordered_food = []
            for food_name in args:
                try:
                    food = [food for food in self.food_menu if food.name == food_name][0]
                    table.order_food(food)
                except IndexError:
                    unordered_food.append(food_name)
            ordered_food_list = "\n".join([repr(ordered_food) for ordered_food in table.food_orders])
            unordered_food_list = "\n".join(unordered_food)
            return f"Table {table_number} ordered:\n" \
                   f"{ordered_food_list}\n" \
                   f"{self.name} does not have in the menu:\n" \
                   f"{unordered_food_list}"

        except IndexError:
            return f"Could not find table {table_number}"

    def order_drink(self, table_number, *args):
        try:
            table = [table for table in self.tables_repository if table.table_number == table_number][0]
            unordered_drinks = []
            for drink_name in args:
                try:
                    drink = [drink for drink in self.drinks_menu if drink.name == drink_name][0]
                    table.order_drink(drink)
                except IndexError:
                    unordered_drinks.append(drink_name)
            ordered_drinks_list = "\n".join(repr(ordered_drink) for ordered_drink in table.drink_orders)
            unordered_drinks_list = "\n".join(unordered_drinks)
            return f"Table {table_number} ordered:\n" \
                   f"{ordered_drinks_list}\n" \
                   f"{self.name} does not have in the menu:\n" \
                   f"{unordered_drinks_list}"

        except IndexError:
            return f"Could not find table {table_number}"

    def leave_table(self, table_number):
        try:
            table = [table for table in self.tables_repository if table.table_number == table_number][0]
            if table.is_reserved:
                bill = table.get_bill()
                table.clear()
                self.total_income += bill
                return f"Table: {table_number}", f"Bill: {bill:.2f}"

        except IndexError:
            pass

    def get_free_tables_info(self):
        info = [table.free_table_info() for table in self.tables_repository if not table.is_reserved]
        return "\n".join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"






