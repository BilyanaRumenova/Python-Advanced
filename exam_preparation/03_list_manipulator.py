from collections import deque


def list_manipulator(numbers, *args):
    numbers = deque(numbers)
    second_param = args[0]
    third_param = args[1]
    if second_param == "add":
        nums_to_add = args[2:]
        if third_param == "beginning":
            nums_to_add = nums_to_add[::-1]
            for el in nums_to_add:
                numbers.appendleft(el)
        elif third_param == "end":
            for el in nums_to_add:
                numbers.append(el)
        return list(numbers)
    elif second_param == "remove":
        if third_param == "beginning":
            if args[2:]:
                for iter in range(args[2]):
                    numbers.popleft()
            else:
                numbers.popleft()
            return list(numbers)
        elif third_param == "end":
            if args[2:]:
                for iter in range(args[2]):
                    numbers.pop()
            else:
                numbers.pop()
            return list(numbers)



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))