SNAKE = "S"
BURROW = "B"
FOOD = "*"
EMPTY = "-"
TRAIL = "."


def read_input():
    size = int(input())
    matrix = [list(input()) for _ in range(size)]
    return matrix


def check_if_inside(cur_row, cur_col, size):
    if 0 <= cur_row < size and 0 <= cur_col < size:
        return True
    return False


def get_snake_position(matrix):
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[0])):
            if matrix[row_index][column_index] == SNAKE:
                return (row_index, column_index)


def get_burrow_position(matrix):
    burrows = 0
    for row_index in range(len(matrix)):
        if BURROW in matrix[row_index]:
            burrows += 1
            if burrows == 2:
                column_index = matrix[row_index].index(BURROW)
                return row_index, column_index


def get_next_move(snake, dir):
    dir_deltas = {"up": (-1, 0), "down": (+1, 0), "left": (0, -1), "right": (0, +1)}
    (row_index, column_index) = snake
    (row_delta, column_delta) = dir_deltas[dir]
    return row_index + row_delta, column_index + column_delta


def check_next_symbol(matrix, snake, direction):
    (row_index, column_index) = snake
    food_quantity = 0
    while food_quantity < 0:
        next_row_index, next_column_index = get_next_move((row_index, column_index), dir)
        matrix[row_index][column_index] = TRAIL
        matrix[next_row_index][next_column_index] = SNAKE
        if matrix[next_row_index][next_column_index] == FOOD:
            food_quantity += 1

        elif matrix[next_row_index][next_column_index] == BURROW:
            burrow_end = get_burrow_position(matrix)
            (burrow_row, burrow_column) = burrow_end
            matrix[burrow_row][burrow_column] = SNAKE
            matrix[next_row_index][next_column_index] = TRAIL

    return matrix, food_quantity


def move_snake(matrix, snake):
    row_index, column_index = snake
    while True:
        direction = input()
        if not check_if_inside(row_index, column_index, len(matrix)):
            matrix[row_index][column_index] = TRAIL
            print("Game over!")
            break
        else:
            matrix[row_index][column_index] = check_next_symbol(matrix, snake, direction)
            food_quantity = check_next_symbol(matrix, snake, direction)[1]
            return food_quantity

    return matrix


def print_result(food, matrix):
    food = move_snake(matrix, snake)[0]
    print(food)
    matrix = move_snake(matrix, snake)[1]


matrix = read_input()
snake = get_snake_position(matrix)
burrow = get_burrow_position(matrix)
food, matrix = move_snake(matrix, snake)

print_result(food, matrix)