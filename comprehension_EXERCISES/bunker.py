categories = {category: [] for category in input().split(", ")}
n = int(input())

quantity = 0
quality = 0

for _ in range(n):
    category, item_name, item_params = input().split(" - ")
    categories[category].append(item_name)

    information_data = item_params.split(";")
    quantity += int(information_data[0].split(":")[1])
    quality += int(information_data[1].split(":")[1])

print(f"Count of items: {quantity}")
print(f"Average quality: {quality/len(categories):.2f}")
[print(f"{category} -> {', '.join(items)}") for category, items in categories.items()]



# bunker = {category: [] for category in input().split(", ")}
# n = int(input())
#
# bunker["count_all_items"] = 0
# bunker["total_quality"] = 0
#
# for _ in range(n):
#     category, item_name, item_params = input().split(" - ")
#     item_quantity = int(item_params.split(";")[0].split(":")[1])
#     item_quality = int(item_params.split(";")[1].split(":")[1])
#     item_data = {item_name: {"quantity": item_quantity, "quality": item_quality}}
#     bunker[category].append(item_data)
#     bunker["count_all_items"] += item_quantity
#     bunker["total_quality"] += item_quality
#
# print(f"Count of items: {bunker['count_all_items']}")
# print(f"Average quality: {(bunker['total_quality']/(len(bunker)-2)):.2f}")
# print(*[f"{category} -> {', '.join([list(d.keys())[0] for d in value])}" for category, value in bunker.items() if isinstance(bunker[category], list)], sep='\n')
#
