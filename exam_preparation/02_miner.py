def read_matrix(size):
    matrix = []
    for row in range(size):
        row = [x for x in input().split()]
        matrix.append(row)
    return matrix


def start_position(matrix):
    total_coals = 0
    for r in range(len(matrix)):
        row = matrix[r]
        for col in range(len(matrix)):
            if row[col] == "s":
                start_pos = [r, col]
            elif row[col] == "c":
                total_coals += 1

    position_x = start_pos[0]
    position_y = start_pos[1]
    return position_check(position_x, position_y, total_coals)


def position_check(x, y, total_coals):
    new_position = ""
    coals = 0
    for direction in directions:
        if direction == "up" and x - 1 >= 0:
            new_position = matrix[x-1][y]
            x -= 1
        elif direction == "down" and x+1 < len(matrix):
            new_position = matrix[x+1][y]
            x += 1
        elif direction == "left" and y-1 >= 0:
            new_position = matrix[x][y-1]
            y -= 1
        elif direction == "right" and y+1 < len(matrix):
            new_position = matrix[x][y+1]
            y += 1
        else:
            continue

        if new_position == "c":
            matrix[x][y] = "*"
            coals += 1
        elif new_position == "e":
            print(f"Game over! ({x}, {y})")
            exit()

        if coals == total_coals and total_coals != 0:
            print(f"You collected all coals! ({x}, {y})")
            exit()
    else:
        print(f"{total_coals - coals} coals left. ({x}, {y})")


size_matrix = int(input())
directions = input().split()

matrix = read_matrix(size_matrix)
start_position(matrix)
