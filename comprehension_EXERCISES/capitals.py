countries = input().split(", ")
capitals = input().split(", ")

# result = {countries[index]: capitals[index] for index in range(len(countries))}
# print(*[f"{country} -> {capital}" for country, capital in result.items()], sep="\n")

result = [f"{countries[index]} -> {capitals[index]}" for index in range(len(countries))]
print(*result, sep="\n")
