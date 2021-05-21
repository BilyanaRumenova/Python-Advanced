def fill_phone_book():
    data = input()
    phone_book = {}
    while not data.isdigit():
        name, phone_number = data.split("-")
        phone_book[name] = phone_number
        data = input()

    return phone_book, int(data)


def search_contact(contact_name, phone_book):
    if contact_name not in phone_book:
        print(f"Contact {contact_name} does not exist.")
    else:
        print(f"{contact_name} -> {phone_book[contact_name]}")


phone_book, iterations_count = fill_phone_book()
for _ in range(int(iterations_count)):
    name = input()
    search_contact(name, phone_book)
