def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


def input_to_list_until_command(end_command):
    lines = []
    while True:
        command = input()
        if command == end_command:
            break
        lines.append(command)

    return lines


def is_vip_guest(guest):
    return guest[0].isdigit()


def separate_into_vip_and_regular(guests):
    vip_guests = []
    regular_guests = []
    for guest in guests:
        if is_vip_guest(guest):
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)
    return (vip_guests, regular_guests)


def print_result(guests):
    print(len(guests))
    (vip_guests, regular_guests) = separate_into_vip_and_regular(guests)

    for guest in sorted(vip_guests):
        print(guest)

    for guest in sorted(regular_guests):
        print(guest)


n_guests = int(input())
reservations = input_to_list(n_guests)
guests_arrived = input_to_list_until_command("END")
guests_not_arrived = set(reservations).difference(guests_arrived)
print_result(guests_not_arrived)

# for guest in guests_arrived:
#     reservations.remove(guest)

# guests_not_arrived = set()
# for guest in reservations:
#     if guest not in guests_arrived:
#         guests_not_arrived.add(guest)

# print(guests_not_arrived)

