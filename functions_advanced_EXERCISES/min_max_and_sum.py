def min_n(nums):
    return min(nums)


def max_n(nums):
    return max(nums)


def sum_nums(nums):
    return sum(nums)


nums = [int(el) for el in input().split()]

print(f"The minimum number is {min_n(nums)}")
print(f"The maximum number is {max_n(nums)}")
print(f"The sum number is: {sum_nums(nums)}")

