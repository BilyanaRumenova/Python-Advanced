def read_matrix(size):
    matrix = []
    for row_index in range(size):
        row = [s for s in input().split()]
        matrix.append(row)
    return matrix


def get_queens_positions(matrix, size):
    queens = []
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "Q":
                q_coordinates = [row, col]
                queens.append(q_coordinates)
    return queens


def is_valid_bound(value, max_value):
    if 0 <= value < max_value:
        return True
    return False


def queen_horizontal_moves(size, matrix, queen_row, queen_col):
    left_queen_col = queen_col - 1
    while is_valid_bound(left_queen_col, size):
        if matrix[queen_row][left_queen_col] == "Q":
            break
        elif matrix[queen_row][left_queen_col] == "K":
            return True
        left_queen_col -= 1

    right_queen_col = queen_col + 1
    while is_valid_bound(right_queen_col, size):
        if matrix[queen_row][right_queen_col] == "Q":
            break
        elif matrix[queen_row][right_queen_col] == "K":
            return True
        right_queen_col += 1


def queen_vertical_moves(size, matrix, queen_row, queen_col):
    up_queen_row = queen_row - 1
    while is_valid_bound(up_queen_row, size):
        if matrix[up_queen_row][queen_col] == "Q":
            break
        elif matrix[up_queen_row][queen_col] == "K":
            return True
        up_queen_row -= 1

    down_queen_row = queen_row + 1
    while is_valid_bound(down_queen_row, size):
        if matrix[down_queen_row][queen_col] == "Q":
            break
        elif matrix[down_queen_row][queen_col] == "K":
            return True
        down_queen_row += 1


def queen_diagonal_moves(size, matrix, queen_row, queen_col):
    #upper left
    up_queen_row = queen_row - 1
    left_queen_col = queen_col - 1
    while is_valid_bound(up_queen_row, size) and is_valid_bound(left_queen_col, size):
        if matrix[up_queen_row][left_queen_col] == "Q":
            break
        elif matrix[up_queen_row][left_queen_col] == "K":
            return True
        up_queen_row -= 1
        left_queen_col -= 1

    #upper right
    up_queen_row = queen_row - 1
    right_queen_col = queen_col + 1
    while is_valid_bound(up_queen_row, size) and is_valid_bound(right_queen_col, size):
        if matrix[up_queen_row][right_queen_col] == "Q":
            break
        elif matrix[up_queen_row][right_queen_col] == "K":
            return True
        up_queen_row -= 1
        right_queen_col += 1

    #down left
    down_queen_row = queen_row + 1
    left_queen_col = queen_col - 1
    while is_valid_bound(down_queen_row, size) and is_valid_bound(left_queen_col, size):
        if matrix[down_queen_row][left_queen_col] == "Q":
            break
        elif matrix[down_queen_row][left_queen_col] == "K":
            return True
        down_queen_row += 1
        left_queen_col -= 1

    #down right
    down_queen_row = queen_row + 1
    right_queen_col = queen_col + 1
    while is_valid_bound(down_queen_row, size) and is_valid_bound(right_queen_col, size):
        if matrix[down_queen_row][right_queen_col] == "Q":
            break
        elif matrix[down_queen_row][right_queen_col] == "K":
            return True
        down_queen_row += 1
        right_queen_col += 1

    # If to the top and to the bottom of the matrix are only '.'
    return False


def check_queens_king_capture(size, matrix, queens):
    queens_capture_king = []
    for queen in queens:
        queen_row = queen[0]
        queen_col = queen[1]
        if queen_horizontal_moves(size, matrix, queen_row, queen_col) or queen_vertical_moves(size, matrix, queen_row, queen_col) or queen_diagonal_moves(size, matrix, queen_row, queen_col):
            queens_capture_king.append(queen)
    return queens_capture_king


def print_result(queens_capture_king):
    if queens_capture_king:
        for queen in queens_capture_king:
            print(queen)
    else:
        print("The king is safe!")


size = 8
matrix = read_matrix(size)
queen_coordinates = get_queens_positions(matrix, size)
queens_capture_king = check_queens_king_capture(size, matrix, queen_coordinates)
print_result(queens_capture_king)

