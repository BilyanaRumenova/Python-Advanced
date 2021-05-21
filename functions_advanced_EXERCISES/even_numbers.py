# def filter_even(iters):
#     return list(filter(lambda x: x % 2 == 0, iters))
#
# numbers = map(int, input().split())
# print(filter_even(numbers))


numbers = map(int, input().split())
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))