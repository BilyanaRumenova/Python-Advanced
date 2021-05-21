text = input()

symbols = {}

for char in text:
    symbols[char] = text.count(char)

sorted_symbols = sorted(symbols.items(), key=lambda x: x[0])
for el in sorted_symbols:
    print(f"{el[0]}: {el[1]} time/s")


# sorted_symbols = sorted(symbols)
# for key in sorted_symbols:
#     print(f"{key}: {symbols[key]} time/s")