n_guests = int(input())

reservations = []

for _ in range(n_guests):
    reservations.append(input())

guests_arrived = []

command = input()
while not command == "END":
    guests_arrived.append(command)

    command = input()

guests_not_arrived = set(reservations).difference(guests_arrived)

vip_guests = []
regular_guests = []

for guest in guests_not_arrived:
    if guest[0].isdigit():
        vip_guests.append(guest)
    else:
        regular_guests.append(guest)

print(len(guests_not_arrived))

for guest in sorted(vip_guests):
    print(guest)

for guest in sorted(regular_guests):
    print(guest)



