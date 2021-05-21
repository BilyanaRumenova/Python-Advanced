from collections import deque

END_COMMAND = 'END'
GREEN_COMMAND = 'green'

green_light = int(input())
free_window = int(input())
pass_time = green_light + free_window

cars = deque()

is_crashed = False
is_closed = False
passed_cars = 0

command = input()
while not command == END_COMMAND:
    if not command == GREEN_COMMAND:
        cars.append(command)
    else:
        for car in range(len(cars)):
            current_car = cars[0]
            if pass_time - free_window <= 0:
                is_closed = True
                break
            elif pass_time >= len(current_car):
                pass_time -= len(current_car)
                cars.popleft()
                passed_cars += 1
            else:
                char = pass_time
                is_crashed = True
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[char]}.")
                break

        pass_time = green_light + free_window

    if is_crashed:
        break

    command = input()

if is_crashed is False:
    print(f"Everyone is safe.\n{passed_cars} total cars passed the crossroads.")