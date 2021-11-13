# from project.rooms.alone_old import AloneOld
# from rooms.young_couple import YoungCouple
# from rooms.young_couple_with_children import YoungCoupleWithChildren
# from people.child import Child


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum(el.expenses + el.room_cost for el in self.rooms)
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        # rooms_to_remove = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                room.budget -= (room.expenses + room.room_cost)
                result.append(f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return "\n".join(result)

    def status(self):
        total_people_in_the_hotel = sum(room.members_count for room in self.rooms)
        status_info = [f"Total population: {total_people_in_the_hotel}"]
        for room in self.rooms:
            status_info.append(f"{room.family_name} with {room.members_count} members. "
                               f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.children:
                for index in range(len(room.children)):
                    monthly_cost = room.children[index].cost * 30
                    status_info.append(f"--- Child {index + 1} monthly cost: {monthly_cost:.2f}$")
            status_info.append(f"--- Appliances monthly cost: {sum(el.get_monthly_expense() for el in room.appliances):.2f}$")

        return "\n".join(status_info)


# everland = Everland()
#
#
# def test_one():
#     young_couple = YoungCouple("Johnsons", 150, 205)
#
#     child1 = Child(5, 1, 2, 1)
#     child2 = Child(3, 2)
#     young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#     single = AloneOld("Petrov", 500)
#     everland.add_room(young_couple)
#     everland.add_room(young_couple_with_children)
#     everland.add_room(single)
#
#     print(everland.get_monthly_consumptions())
#     print(everland.pay())
#     print(everland.status())
#
#
#
# test_one()
