from collections import deque

males = [int(el) for el in input().split()]
females = [int(el) for el in input().split()]

females = deque(females)

matches = 0

while males and females:
    current_female = females[0]
    current_male = males[-1]
    if current_male <= 0:
        males.pop()
        continue

    if current_female <= 0:
        females.popleft()
        continue

    if current_male % 25 == 0:
        males.pop()
        males.pop()
        continue

    if current_female % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if current_female == current_male:
        females.popleft()
        males.pop()
        matches += 1
    else:
        females.popleft()
        males[-1] -= 2


print(f"Matches: {matches}")
if males:
    males = [str(el) for el in reversed(males)]
    print(f"Males left: {', '.join(males)}")
else:
    print("Males left: none")

if females:
    females = [str(el) for el in females]
    print(f"Females left: {', '.join(females)}")
else:
    print("Females left: none")

