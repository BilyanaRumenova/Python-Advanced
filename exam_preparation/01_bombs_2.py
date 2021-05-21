from collections import deque

def check_if_successfully(bomb_dict):
    count = 0
    for key in bomb_dict:
        if bomb_dict[key] >= 3:
            count += 1

    if count == 3:
        return True
    return False


bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_casings = [int(el) for el in input().split(", ")]

# DATURA_BOMBS = 40
# CHERRY_BOMBS = 60
# SMOKE_DEKOY_BOMBS = 120

bombs = {40: 0, 60: 0, 120: 0}
is_successfully = False

count_datura = 0
count_cherry = 0
count_smoke_dekoy = 0

while bomb_effects and bomb_casings:

    if check_if_successfully(bombs):
        is_successfully = True
        break

    sum_of_bomb_effect_and_casing = bomb_effects[0] + bomb_casings[-1]

    if sum_of_bomb_effect_and_casing in bombs:
        bombs[sum_of_bomb_effect_and_casing] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5


if is_successfully:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(el) for el in bomb_casings])}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {bombs[60]}")
print(f"Datura Bombs: {bombs[40]}")
print(f"Smoke Decoy Bombs: {bombs[120]}")


