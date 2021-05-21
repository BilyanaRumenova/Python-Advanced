def odd(nums):
    odd_sum = sum(filter(lambda x: x % 2 == 1, nums))
    return odd_sum * len(nums)


def even(nums):
    even_sum = sum(filter(lambda x: x % 2 == 0, nums))
    return even_sum * len(nums)


command = input()
nums = [int(el) for el in input().split()]

if command == "Odd":
    print(odd(nums))
else:
    print(even(nums))