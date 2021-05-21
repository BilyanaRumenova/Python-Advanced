rows, cols = [int(el) for el in input().split()]


def init_matrix():
    matrix = []
    for _ in range(rows):
        elements = [int(el) for el in input().split()]
        matrix.append(elements)
    return matrix


def get_sub_matrix_sum(matr, row_i, col_i):
    the_sum = 0
    for r in range(row_i, row_i+3):
        for c in range(col_i, col_i+3):
            the_sum += matr[r][c]
    return the_sum


matrix = init_matrix()
best_value = get_sub_matrix_sum(matrix, 0, 0)
best_position = (0, 0)

for row_index in range(rows-2):
    for col_index in range(cols-2):
        current_value = get_sub_matrix_sum(matrix, row_index, col_index)
        if best_value < current_value:
            best_value = current_value
            best_position = (row_index, col_index)

print(f"Sum = {best_value}")
best_row, best_col = best_position
for r in range(best_row, best_row+3):
        for c in range(best_col, best_col+3):
            print(matrix[r][c], end=" ")
        print()