size_matrix = int(input())
number_of_bombs = int(input())

matrix = [[0] * size_matrix for _ in range(size_matrix)]


def is_valid_bound(new_row, new_col, size_matrix):
    if 0 <= new_row < size_matrix and 0 <= new_col < size_matrix:
        return True
    return False


def calculate_near_bombs(cur_row, cur_col, matrix):
    bomb_neighbours = 0
    # up, down, left, right, upper left diagonal, upper right diagonal, lower left diagonal, lower right diagonal
    rows = [-1, 1, 0, 0, -1, -1, 1, 1]
    cols = [0, 0, -1, 1, -1, 1, -1, 1]
    for i in range(8):
        new_row = cur_row + rows[i]
        new_col = cur_col + cols[i]
        if is_valid_bound(new_row, new_col, len(matrix)):
            if matrix[new_row][new_col] == "*":
                bomb_neighbours += 1
    return bomb_neighbours


for _ in range(number_of_bombs):
    bomb_position = input().split(', ')
    row = int(bomb_position[0].strip("()"))
    col = int(bomb_position[1].strip("()"))
    matrix[row][col] = "*"

for row in range(size_matrix):
    for col in range(size_matrix):
        if not matrix[row][col] == "*":
            cell_value = calculate_near_bombs(row, col, matrix)
            matrix[row][col] = cell_value

for row in matrix:
    print(" ".join([str(el) for el in row]))