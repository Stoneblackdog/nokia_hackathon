#!/usr/bin/env python3

from maze import solve_maze

with open('./input.txt', 'r') as f:
    input = f.read()
    maze_a_and_b_c = input.strip().split('B')  # [A, BC]
    maze_a = maze_a_and_b_c[0].replace('A', '')
    maze_b = maze_a_and_b_c[1].split('C')[0]
    maze_c = maze_a_and_b_c[1].split('C')[1]
    solution_a = solve_maze(maze_a)
    solution_b = solve_maze(maze_b)
    solution_c = solve_maze(maze_c)

    print('A')
    print(*solution_a, sep=' ')
    print()
    print('B')
    print(*solution_b, sep=' ')
    print()
    print('C')
    print(*solution_c, sep=' ')
