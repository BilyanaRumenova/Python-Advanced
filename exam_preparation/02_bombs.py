def read_matrix():
    size = int(input())
    matrix = []
    for row in range(size):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def check_if_index_is_valid(pottential_row, pottential_col, size):
    if 0 <= pottential_row < size and 0 <= pottential_col < size:
        return True
    return False


def bomb_explosion(bombs, matrix):
    row, col = [int(x) for x in bombs.split(",")]
    bomb_range = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row_step, col_step in bomb_range:
        pottential_row = row + row_step
        pottential_col = col + col_step

        if check_if_index_is_valid(pottential_row, pottential_col, len(matrix)):
            if matrix[pottential_row][pottential_col] > 0:
                matrix[pottential_row][pottential_col] -= matrix[row][col]

    if matrix[row][col] > 0:
        matrix[row][col] = 0
    return matrix


def get_active_cells(matrix):
    size = len(matrix)
    active_cells = 0
    sum_active_sells = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] > 0:
                active_cells += 1
                sum_active_sells += matrix[r][c]
    return active_cells, sum_active_sells


def print_result(active_cells, sum_active_cells, matrix):
    print(f"Alive cells: {active_cells}")
    print(f"Sum: {sum_active_cells}")
    for row in range(len(matrix)):
        print(" ".join(str(x) for x in matrix[row]))


matrix = read_matrix()
bombs = input().split()

for bomb_coords in range(len(bombs)):
    bomb_explosion(bombs[bomb_coords], matrix)

active_cells = get_active_cells(matrix)[0]
sum_active_cells = get_active_cells(matrix)[1]

print_result(active_cells, sum_active_cells, matrix)




