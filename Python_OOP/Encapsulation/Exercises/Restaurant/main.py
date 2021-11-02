from Encapsulation.Exercises.Restaurant.project.beverage.beverage import Beverage
from Encapsulation.Exercises.Restaurant.project.food.soup import Soup
from Encapsulation.Exercises.Restaurant.project.product import Product

product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)
