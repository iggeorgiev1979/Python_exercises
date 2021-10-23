n = int(input())
vip_guests = set()
regular_guests = set()
for _ in range(n):
    guest = input()
    if guest[0].isnumeric() and len(guest) == 8:
        vip_guests.add(guest)
    elif len(guest) == 8:
        regular_guests.add(guest)
guest = input()
while not guest == 'END':
    if guest in vip_guests:
        vip_guests.remove(guest)
    elif guest in regular_guests:
        regular_guests.remove(guest)
    guest = input()
# total_missing_guests = len(vip_guests) + len(regular_guests)


print(len(vip_guests) + len(regular_guests))
print(*sorted(vip_guests), sep='\n')
print(*sorted(regular_guests), sep='\n')
