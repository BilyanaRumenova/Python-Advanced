rows, cols = [int(el) for el in input().split()]

def init_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        elements = input().split()
        matrix.append(elements)
    return matrix


def check_if_index_is_valid(index_row, index_cols, rows, cols):
     if 0 <= index_row < rows and 0 <= index_cols < cols:
         return True
     return False


def check_if_command_is_valid(command, coords, rows, cols):
    if len(coords) == 4 and command == "swap":
        for index in range(0, len(coords), 2):
            if not check_if_index_is_valid(coords[index], coords[index+1], rows, cols):
                print("Invalid input!")
                return False
        return True
    print("Invalid input!")
    return False


def print_matrix(matrix):
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            print(f"{matrix[row_index][col_index]} ", end="")
        print()


matrix = init_matrix(rows, cols)

data = input()

while not data == "END":
    split_data = data.split()
    try:
        command = split_data[0]
        coordinates = [int(el) for el in split_data[1:]]
    except:
        print("Invalid input!")
    if check_if_command_is_valid(command, coordinates, rows, cols):
        current_row = coordinates[0]
        current_col = coordinates[1]
        row_to_swap = coordinates[2]
        col_to_swap = coordinates[3]
        temp = matrix[current_row][current_col]
        matrix[current_row][current_col] = matrix[row_to_swap][col_to_swap]
        matrix[row_to_swap][col_to_swap] = temp
        print_matrix(matrix)

    data = input()