with open("numbers.txt", "r") as file:
    # print(sum([int(el[:-1]) for el in file.readlines()]))
    print(sum([int(el.strip()) for el in file.readlines()]))