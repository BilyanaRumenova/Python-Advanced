from collections import deque

food_quantity = int(input())
order_quantity = list(map(int, input().split()))

orders = deque(order_quantity)

print(max(orders))

while orders:
    current_order = orders[0]

    if current_order <= food_quantity:
        food_quantity -= current_order
        orders.popleft()
    else:
        break

if orders:
    result = ""
    for el in orders:
        result += str(el) + " "
    print(f"Orders left: {result}")
else:
    print("Orders complete")