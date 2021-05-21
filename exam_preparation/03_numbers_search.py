def numbers_searching(*args):
    dublicates = []
    missing_num = 0
    numbers = list(args)
    min_num = min(numbers)
    max_num = max(numbers)
    for num in range(min_num, max_num+1):
        if num not in numbers:
            missing_num = num

    for num in numbers:
        if numbers.count(num) > 1 and num not in dublicates:
            dublicates.append(num)

        dublicates = sorted(dublicates)

    return [missing_num, dublicates]

print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))