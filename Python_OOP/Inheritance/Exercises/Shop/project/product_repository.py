# from Inheritance.Exercises.Shop.project.drink import Drink
# from Inheritance.Exercises.Shop.project.food import Food
from project.drink import Drink
from project.food import Food


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name: str):
        for obj in self.products:
            if obj.name == product_name:
                return obj

    def remove(self, product_name):
        for obj in self.products:
            if obj.name == product_name:
                self.products.remove(obj)
                break

    def __repr__(self):
        tmp_list = [f"{obj.name}: {obj.quantity}" for obj in self.products]
        return "\n".join(tmp_list)

# drink = Drink("Soda")
# food = Food("Stake")
#
# store = ProductRepository()
# store.add(drink)
# store.add(food)
# store.remove("Soda")
# print(store)
