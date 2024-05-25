#!/usr/bin/env python3

from matrix import scan_matrix, add_matrices, multiply_matrices, create_empty_matrix
from parser import Parser, Node


def walk_ast(root_node: Node, matrices: dict):
    current_node = root_node
    if current_node.value == '+':
        result = add_matrices(walk_ast(current_node.left, matrices), walk_ast(current_node.right, matrices))
    elif current_node.value == '*':
        result = multiply_matrices(walk_ast(current_node.left, matrices), walk_ast(current_node.right, matrices))
    elif current_node.value.isalpha():
        result = matrices[current_node.value]

    return result

def do_operation(operation: str, matrices: dict):
    operation = operation.split(' ')
    parser = Parser(operation)
    root_node = parser.parse_expression()

    return walk_ast(root_node, matrices)


def scan_operations(lines: list):
    start = lines.index('operations') + 1
    operations = []

    for i in range(start, len(lines)):
        operations.append(lines[i])

    return operations


with open('./input.txt', 'r') as f:
    input = f.readlines()
    lines = list(map(lambda line: line.strip(), input))
    lines = list(filter(None, lines))
    matrices = {
        'A': scan_matrix(lines, 'A'),
        'B': scan_matrix(lines, 'B'),
        'C': scan_matrix(lines, 'C'),
        'D': scan_matrix(lines, 'D'),
        'E': scan_matrix(lines, 'E'),
        'F': scan_matrix(lines, 'F'),
        'G': scan_matrix(lines, 'G'),
        'H': scan_matrix(lines, 'H'),
        'I': scan_matrix(lines, 'I'),
        'J': scan_matrix(lines, 'J'),
    }
    operations = scan_operations(lines)

    print('\n')
    for operation in operations:
        print(operation)
        for line in do_operation(operation, matrices):
            for number in line:
                print(number, end=' ')
            print()
        print()
