def str_to_int(strings):
    return [int(x) for x in strings]


def read_matrix():
    rows_count = int(input())
    return [str_to_int(input().split(', ')) for _ in range(rows_count)]


def get_even_matrix(matrix):
    return [[int(x) for x in row if x % 2 == 0]for row in matrix]


def print_result(matrix):
    print(matrix)


matrix = read_matrix()
even_matrix = get_even_matrix(matrix)
print_result(even_matrix)
