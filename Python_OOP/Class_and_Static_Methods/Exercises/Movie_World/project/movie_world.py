from Class_and_Static_Methods.Exercises.Movie_World.project.customer import Customer
from Class_and_Static_Methods.Exercises.Movie_World.project.dvd import DVD


# from project.customer import Customer
# from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        tmp = [element for element in self.customers if element.id == customer_id]
        customer, = tmp if tmp else None
        if customer:
            tmp = [element for element in self.dvds if element.id == dvd_id]
            dvd, = tmp if tmp else None
            if dvd:
                if dvd in customer.rented_dvds:
                    return f"{customer.name} has already rented {dvd.name}"
                if dvd.is_rented:
                    return "DVD is already rented"
                if customer.age < dvd.age_restriction:
                    return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                dvd.is_rented = True
                customer.rented_dvds.append(dvd)
                return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        tmp = [element for element in self.customers if element.id == customer_id]
        if tmp:
            customer = tmp[0]
        else:
            customer = None
        if customer:
            tmp = [element for element in customer.rented_dvds if element.id == dvd_id]
            if tmp:
                dvd = tmp[0]
            else:
                dvd = None
            if dvd:
                customer.rented_dvds.remove(dvd)
                dvd.is_rented = False
                return f"{customer.name} has successfully returned {dvd.name}"
            return f"{customer.name} does not have that DVD"

    def generate_customers_list(self):
        result_list = [f"{x}" for x in self.customers]
        result_list.extend([f"{element}" for element in self.dvds])
        return result_list

    def __repr__(self):
        return '\n'.join(self.generate_customers_list())

# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 10)
# c = Customer("Pesho", 20, 4)
# movie_world.add_customer(c)
# movie_world.add_dvd(d)
# result = movie_world.return_dvd(4, 1)
# print(result, "Pesho does not have that DVD")
