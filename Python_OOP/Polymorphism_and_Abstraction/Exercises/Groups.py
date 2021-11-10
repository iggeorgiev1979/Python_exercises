class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return self.create_new_instance(self.name, other.surname)

    @classmethod
    def create_new_instance(cls, name, surname):
        return cls(name, surname)

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_name = f"{self.name} {other.name}"
        new_people_list = self.people.copy()
        new_people_list.extend(other.people)
        return self.create_new_group(new_name, new_people_list)

    def __getitem__(self, item):
        return f"Person {item}: {repr(self.people[item])}"

    @classmethod
    def create_new_group(cls, name, people):
        return cls(name, people)

    def __repr__(self):
        persons = [f"{el}" for el in self.people]
        return f"Group {self.name} with members {', '.join(persons)}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
