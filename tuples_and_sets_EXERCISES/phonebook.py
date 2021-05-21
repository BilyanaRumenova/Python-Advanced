data = input()

phone_book = {}

while not data.isdigit():
    name, phone_number = data.split("-")
    phone_book[name] = phone_number

    data = input()

for _ in range(int(data)):
    name = input()

    if phone_book.get(name):
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")


# for _ in range(int(data)):
#     name = input()
#
#     if name not in phone_book:
#         print(f"Contact {name} does not exist.")
#     else:
#         print(f"{name} -> {phone_book[name]}")