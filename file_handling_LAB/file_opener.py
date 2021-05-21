try:
    with open("text_.txt") as file:
        print("File found")
except FileNotFoundError:
    print("File not found")

