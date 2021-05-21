nums = list(map(int, input().split()))

s = []

for n in nums:
    s.append(n)

reversed_nums = []

while s:
    reversed_nums.append(s.pop())

print(*reversed_nums)

