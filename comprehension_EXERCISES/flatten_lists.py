# result = [" ".join(list_as_str.split()) for list_as_str in input().split('|')[::-1]]
# print(*result)

# result = [value.strip() for iteration in range(len(data)) for value in data[iteration].split()]

data = input().split("|")
data.reverse()

result = []
for iteration in range(len(data)):
    for value in data[iteration].split():
        result.append(value)

print(*result)