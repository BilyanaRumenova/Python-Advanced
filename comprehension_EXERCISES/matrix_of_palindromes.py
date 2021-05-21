# rows, cols = [int(el) for el in input().split()]
#
# result = [[f"{chr(num)}{chr(nested_num)}{chr(num)}" for nested_num in range(num, num+cols)] for num in range(97, 97+rows)]
#
# print(*[" ".join(iterable) for iterable in result], sep="\n")

def ascii_to_char(row, cols):
    return [(chr(97+row) + chr(97+row+col) + chr(97+row)) for col in range(0, cols)]


def generate_palindromes(rows, cols):
    matrix = [ascii_to_char(row, cols) for row in range(rows)]
    return matrix


def print_result(matrix):
    for row in matrix:
        print(*row)
    return matrix


rows, cols = [int(el) for el in input().split()]
matrix = generate_palindromes(rows, cols)
print_result(matrix)
