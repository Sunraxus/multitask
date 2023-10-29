import concurrent.futures
import sys

def calculate_line_sum(line):
    return sum(line)

def calculate_column_sum(column_index, matrix):
    column_sum = 0
    for line in matrix:
        column_sum += line[column_index]
    return column_sum

if __name__ == "__main__":
    matrix_size = int(sys.argv[1])
    matrix_values = list(map(int, sys.argv[2:]))
    if len(matrix_values) != matrix_size * matrix_size:
        print("Неверное количество значений.")
        sys.exit(1)
    
    matrix = [matrix_values[i:i + matrix_size] for i in range(0, len(matrix_values), matrix_size)]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        line_sums = list(executor.map(calculate_line_sum, matrix))
        column_sums = list(executor.map(calculate_column_sum, range(matrix_size), [matrix]*matrix_size))

    total_sum = sum(line_sums)

    print("Матрица:")
    for line in matrix:
        print(line)

    print("Суммы строк:", line_sums)
    print("Суммы столбцов:", column_sums)
    print("Общая сумма:", total_sum)