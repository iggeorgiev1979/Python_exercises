from Class_and_Static_Methods.Exercises.Gym.project.customer import Customer
from Class_and_Static_Methods.Exercises.Gym.project.equipment import Equipment
from Class_and_Static_Methods.Exercises.Gym.project.exercise_plan import ExercisePlan
from Class_and_Static_Methods.Exercises.Gym.project.subscription import Subscription
from Class_and_Static_Methods.Exercises.Gym.project.trainer import Trainer
# from project.customer import Customer
# from project.equipment import Equipment
# from project.exercise_plan import ExercisePlan
# from project.subscription import Subscription
# from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.__get_subscription(subscription_id)
        plan = self.__get_exercise_plan(subscription.exercise_id)
        customer = self.__get_customer(subscription.customer_id)
        trainer = self.__get_trainer(subscription.trainer_id)
        equipment = self.__get_equipment(plan.equipment_id)
        return f"{subscription}\n" \
               f"{customer}\n" \
               f"{trainer}\n" \
               f"{equipment}\n" \
               f"{plan}"

    def __get_subscription(self, subscription_id):
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                return subscription

    def __get_exercise_plan(self, exercise_id):
        for exercise in self.plans:
            if exercise.id == exercise_id:
                return exercise

    def __get_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def __get_trainer(self, trainer_id):
        for trainer in self.trainers:
            if trainer.id == trainer_id:
                return trainer

    def __get_equipment(self, equipment_id):
        for equipment in self.equipment:
            if equipment.id == equipment_id:
                return equipment

# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
#
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))
