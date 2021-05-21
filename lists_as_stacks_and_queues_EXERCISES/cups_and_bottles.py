from collections import deque

cups_capacity = list(map(int, input().split()))
bottles = list(map(int, input().split()))

cups = deque(cups_capacity)

wasted_water = 0

while len(cups) > 0 and len(bottles) > 0:

    current_cup = cups[0]
    current_bottle = bottles[-1]

    if current_cup > current_bottle:
        reduced_cup_value = current_cup - current_bottle
        current_bottle = bottles.pop()

        while reduced_cup_value > 0 and len(bottles) > 0:
            next_bottle = bottles[-1]
            if next_bottle > reduced_cup_value:
                wasted_water += (next_bottle - reduced_cup_value)
                reduced_cup_value -= next_bottle
            else:
                reduced_cup_value -= next_bottle
            bottles.pop()

        cups.popleft()
    else:
        wasted_water += current_bottle - current_cup
        bottles.pop()
        cups.popleft()

if len(bottles) > 0:
    print(f"Bottles: {' '.join(map(str, bottles))}")

elif len(cups) > 0:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_water}")


