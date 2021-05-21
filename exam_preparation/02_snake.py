size_matrix = int(input())
matrix = [list(input()) for _ in range(size_matrix)]


def check_starting_position(matrix, start):
    for row in range(len(matrix)):
        if start in matrix[row]:
            return row, matrix[row].index(start)


def check_if_inside(cur_row, cur_col, size):
    if 0 <= cur_row < size and 0 <= cur_col < size:
        return True
    return False


def find_burrow(matrix, burrow):
    burrows = 0
    for row_i in range(len(matrix)):
        if burrow in matrix[row_i]:
            burrows += 1
            if burrows == 2:
                return row_i, matrix[row_i].index(burrow)


def print_result(matrix):
    for row in range(len(matrix)):
        print("".join(matrix[row]))


START = 'S'
BURROW = 'B'

UP_MOVE = (-1, 0)
DOWN_MOVE = (1, 0)
LEFT_MOVE = (0, -1)
RIGHT_MOVE = (0, 1)

starting_row, starting_col = check_starting_position(matrix, START)
food_quantity = 0
current_row, current_col = starting_row, starting_col

while True:
    direction = input()

    last_row, last_col = current_row, current_col
    if direction == "up":
        current_row += UP_MOVE[0]
        current_col += UP_MOVE[1]
    elif direction == "down":
        current_row += DOWN_MOVE[0]
        current_col += DOWN_MOVE[1]
    elif direction == "left":
        current_row += LEFT_MOVE[0]
        current_col += LEFT_MOVE[1]
    elif direction == "right":
        current_row += RIGHT_MOVE[0]
        current_col += RIGHT_MOVE[1]

    if not check_if_inside(current_row, current_col, size_matrix):
        matrix[last_row][last_col] = "."
        print("Game over!")
        break

    if matrix[current_row][current_col] == "*":
        food_quantity += 1
        matrix[last_row][last_col] = "."
        matrix[current_row][current_col] = "S"
        if food_quantity >= 10:
            break

    elif matrix[current_row][current_col] == "-":
        matrix[last_row][last_col] = "."
        matrix[current_row][current_col] = "S"

    elif matrix[current_row][current_col] == 'B':
        burrow_end_position = find_burrow(matrix, BURROW)
        matrix[last_row][last_col] = "."
        matrix[current_row][current_col] = "."
        current_row, current_col = burrow_end_position[0], burrow_end_position[1]
        matrix[current_row][current_col] = 'S'

if food_quantity >= 10:
    print(f"You won! You fed the snake.")

print(f"Food eaten: {food_quantity}")
print_result(matrix)



