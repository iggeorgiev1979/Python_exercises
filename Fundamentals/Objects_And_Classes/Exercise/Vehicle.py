class Vehicle:
    def __init__(self, type, model, price):
        self.owner = None
        self.type = type
        self.model = model
        self.price = price

    def buy(self, money, owner):
        if self.owner:
            return "Car already sold"
        elif self.price > money:
            return "Sorry, not enough money"
        else:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"

    def sell(self):
        if not self.owner:
            return "Vehicle has no owner"
        self.owner = None

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"


v_type = "car"
model_car = "BMW"
price_car = 30000
vehicle = Vehicle(v_type, model_car, price_car)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)
