import re


def scan_matrix(lines: list, label: str):
    start = lines.index(label)
    matrix = []

    for i in range(start + 1, len(lines)):
        if re.search('[a-zA-Z]', lines[i]):
            break
        # append list of numbers to matrix, converted to integers
        matrix.append(list(map(lambda x: int(x), lines[i].split())))

    return matrix


def create_empty_matrix(rows: int, cols: int):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def add_matrices(mat_a: list, mat_b: list):
    # return if matrices are not the same size
    if len(mat_a) != len(mat_b) or len(mat_a[0]) != len(mat_b[0]):
        return

    mat_c = create_empty_matrix(len(mat_a), len(mat_a[0]))
    for row in range(len(mat_c)):
        for col in range(len(mat_c[0])):
            mat_c[row][col] = mat_a[row][col] + mat_b[row][col]

    return mat_c


def multiply_matrices(mat_a: list, mat_b: list):
    if len(mat_a[0]) != len(mat_b):
        return

    mat_c = create_empty_matrix(len(mat_a), len(mat_b[0]))
    for i in range(len(mat_a)):
        for j in range(len(mat_b[0])):
            for k in range(len(mat_a[0])):
                mat_c[i][j] += mat_a[i][k] * mat_b[k][j]

    return mat_c
