sets_length = input().split()
n, m = int(sets_length[0]), int(sets_length[1])

set_n = set()
set_m = set()

for _ in range(n):
    num_n = int(input())
    set_n.add(num_n)

for _ in range(m):
    num_m = int(input())
    set_m.add(num_m)

unique = set_n.intersection(set_m)
for el in unique:
    print(el)