n = int(input())

intersections = []

for _ in range(n):
    data = input()

    first_data, second_data = data.split("-")
    start_1, end_1 = [int(el) for el in first_data.split(",")]
    start_2, end_2 = [int(el) for el in second_data.split(",")]

    intersection = range(max(start_1, start_2), min(end_1, end_2)+1)
    intersections.append(intersection)

longest = sorted(intersections, key=lambda x: -len(x))[0]


print(f"Longest intersection is {list(longest)} with length {len(longest)}")




# n = int(input())
#
# intersections = []
#
# for _ in range(n):
#     data = input()
#
#     first_data, second_data = data.split("-")
#     start_1, end_1 = [int(el) for el in first_data.split(",")]
#     start_2, end_2 = [int(el) for el in second_data.split(",")]
#     first_seq = range(start_1, end_1+1)
#     second_seq = range(start_2, end_2+1)
#     intersection = set(first_seq).intersection(second_seq)
#     intersections.append(intersection)
#
# longest = sorted(intersections, key=lambda x: -len(x))[0]
#
#
# print(f"Longest intersection is {list(longest)} with length {len(longest)}")
