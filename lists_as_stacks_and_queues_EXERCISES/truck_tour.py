from collections import deque

n = int(input())

stations = deque([])

for _ in range(n):
    stations.append(input())


for big_circle_iteration in range(n):
    is_valid = True
    petrol_in_tank = 0

    for small_circle_iteration in range(n):
        current_station = stations[big_circle_iteration]

        petrol, distance_to_next_station = current_station.split()
        petrol = int(petrol)
        distance_to_next_station = int(distance_to_next_station)
        petrol_in_tank += distance_to_next_station

        if petrol_in_tank >= distance_to_next_station:
            petrol_in_tank -= distance_to_next_station
            stations.append(stations.popleft())
        else:
            is_valid = False
            break

    if is_valid:
        print(big_circle_iteration)
        break



