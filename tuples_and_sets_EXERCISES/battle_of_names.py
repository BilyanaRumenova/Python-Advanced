n = int(input())

even_sum = set()
odd_sum = set()

for line in range(1, n+1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // line

    if current_sum % 2 == 0:
        even_sum.add(current_sum)
    else:
        odd_sum.add(current_sum)

total_sum_even = sum(even_sum)
total_sum_odd = sum(odd_sum)

if total_sum_even == total_sum_odd:
    modified_set = [str(el) for el in even_sum.union(odd_sum)]
    print(f"{', '.join(modified_set)}")
elif total_sum_odd > total_sum_even:
    modified_set = [str(el) for el in odd_sum.difference(even_sum)]
    print(f"{', '.join(modified_set)}")
else:
    modified_set = [str(el) for el in odd_sum.symmetric_difference(even_sum)]
    print(f"{', '.join(modified_set)}")