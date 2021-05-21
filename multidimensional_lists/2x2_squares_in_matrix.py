rows, cols = [int(el) for el in input().split()]

def init_matrix():
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())
    return matrix


def check_if_elements_are_equal(row_i, col_i, matr):
    current_el = matr[row_i][col_i]
    next_el_same_row = matr[row_i][col_i+1]
    el_below = matr[row_i+1][col_i]
    el_below_right = matr[row_i+1][col_i+1]
    if current_el == next_el_same_row == el_below == el_below_right:
        return True
    return False


matrix = init_matrix()
counter = 0

for row_index in range(rows-1):
    for col_index in range(cols-1):
        if check_if_elements_are_equal(row_index, col_index, matrix):
            counter += 1

print(counter)