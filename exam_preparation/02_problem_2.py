string = input()

PLAYER_SYMBOL = "P"

# directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

UP_MOVE = (-1, 0)
DOWN_MOVE = (1, 0)
LEFT_MOVE = (0, -1)
RIGHT_MOVE = (0, 1)


def read_field():
    size = int(input())
    field = [list(input()) for _ in range(size)]
    return field


def find_player_position(field):
    for row_index in range(len(field)):
        if PLAYER_SYMBOL in field[row_index]:
            column_index = field[row_index].index(PLAYER_SYMBOL)
            return (row_index, column_index)


def in_range(value, max_value):
    return 0 <= value < max_value


def move(field, player, string):
    m = int(input())
    (starting_row, starting_col) = player
    current_row, current_col = starting_row, starting_col
    for _ in range(m):
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

        if not in_range(current_row, len(field)) or not in_range(current_col, len(field[0])):
            if len(string) > 0:
                string = string[:-1]
                current_row = last_row
                current_col = last_col

        else:
            if field[current_row][current_col].isalpha():
                string += field[current_row][current_col]

        field[last_row][last_col] = "-"
        field[current_row][current_col] = PLAYER_SYMBOL
    return string, field


def print_result(results):
    new_string = results[0]
    new_field = results[1]
    print(new_string)

    for row in new_field:
        print(*row, sep="")


field = read_field()
player = find_player_position(field)
results = move(field, player, string)
print_result(results)