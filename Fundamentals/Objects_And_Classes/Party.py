class Party:
    def __init__(self):
        self.people = []


my_list = Party()
names = input()
while not names == 'End':
    my_list.people.append(names)
    names = input()
print(f'Going: {", ".join(my_list.people)}')
print(f'Total: {len(my_list.people)}')
