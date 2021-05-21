n = int(input())

chemical_compounds = set()

for _ in range(n):
    compounds = input().split()
    for el in compounds:
        chemical_compounds.add(el)

for el in chemical_compounds:
    print(el)