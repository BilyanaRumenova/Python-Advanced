box = list(map(int, input().split()))
capacity = int(input())

racks = 1

current_capacity = capacity

while len(box) > 0:
    current_v_clothes = box.pop()

    if current_v_clothes <= current_capacity:
        current_capacity -= current_v_clothes
    else:
        racks += 1
        current_capacity = capacity
        current_capacity -= current_v_clothes

print(racks)