def round_iterable_elements(nums_list):
    result = [round(el) for el in nums_list]
    return result


# nums = [float(el) for el in input().split()]
nums = map(float, input().split())
print(round_iterable_elements(nums))
