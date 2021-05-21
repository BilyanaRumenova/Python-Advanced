rows_count = int(input())


def read_matrix():
    matrix = []
    for _ in range(rows_count):
        matrix.append([int(el) for el in input().split()])
    return matrix


# def read_matrix():
#     matrix = [[int(el) for el in input().split()] for _ in range(rows_count)]
#     return matrix


def check_if_index_is_valid(coords):
    index_row, index_cols = coords
    if 0 <= index_row < rows_count and 0 <= index_cols < rows_count:
        return True
    print("Invalid coordinates")
    return False


def add(matrix, coords, value):
    row, col = coords[0], coords[1]
    matrix[row][col] += value
    return matrix


def substract(matrix, coords, value):
    row, col = coords[0], coords[1]
    matrix[row][col] -= value
    return matrix


def print_result(matrix):
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            print(f"{matrix[row_index][col_index]} ", end="")
        print()


matrix = read_matrix()

data = input()

while not data == "END":
    split_data = data.split()
    command = split_data[0]
    coordinates = [int(el) for el in split_data[1:3]]
    value = int(split_data[3])

    if check_if_index_is_valid(coordinates):
        if command == "Add":
            add(matrix, coordinates, value)
        else:
            substract(matrix, coordinates, value)

    data = input()

print_result(matrix)