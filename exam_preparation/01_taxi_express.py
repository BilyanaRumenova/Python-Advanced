from collections import deque

customers = deque([int(el) for el in input().split(", ")])
taxis = [int(el) for el in input().split(", ")]

total_time = 0

while customers and taxis:
    current_customer = customers[0]
    current_taxi = taxis[-1]

    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

elif not taxis and len(customers) > 0:
    customers = [str(el) for el in customers]
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(customers)}")