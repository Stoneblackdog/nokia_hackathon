class Node:
    def __init__(self, ty):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.ty = ty
        self.visited = False
        self.came_from = None


def create_graph(maze: str):
    # Transform maze into more usable variant without spaces or newlines
    maze = maze.replace(' ', '').split('\n')
    maze = list(filter(None, maze))
    # "Swap" characters for nodes
    node_matrix = [[Node(ty) for ty in line] for line in maze]
    start = None

    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == '#':
                continue
            if node_matrix[y - 1][x].ty != '#':
                node_matrix[y][x].up = node_matrix[y - 1][x]
            if node_matrix[y + 1][x].ty != '#':
                node_matrix[y][x].down = node_matrix[y + 1][x]
            if node_matrix[y][x - 1].ty != '#':
                node_matrix[y][x].left = node_matrix[y][x - 1]
            if node_matrix[y][x + 1].ty != '#':
                node_matrix[y][x].right = node_matrix[y][x + 1]
            if char == 'S':
                start = node_matrix[y][x]

    return start


def find_destination_node(open_nodes: list):
    new_open_nodes = []
    while True:
        for node in open_nodes:
            if node.ty == 'G':
                return node
            if node.up is not None and node.up.visited is False:
                node.up.came_from = node
                new_open_nodes.append(node.up)
            if node.down is not None and node.down.visited is False:
                node.down.came_from = node
                new_open_nodes.append(node.down)
            if node.left is not None and node.left.visited is False:
                node.left.came_from = node
                new_open_nodes.append(node.left)
            if node.right is not None and node.right.visited is False:
                node.right.came_from = node
                new_open_nodes.append(node.right)
            node.visited = True
        open_nodes = new_open_nodes


def solve_maze(maze: str):
    start = create_graph(maze)
    solution = ['S']
    stack = []
    open_nodes = [start]

    current_node = find_destination_node(open_nodes)
    while True:
        stack.append(current_node)
        if current_node.ty == 'S':
            break
        current_node = current_node.came_from

    while current_node.ty != 'G':
        popped_node = stack.pop()
        if popped_node == current_node.up:
            solution.append('U')
        elif popped_node == current_node.down:
            solution.append('D')
        elif popped_node == current_node.left:
            solution.append('L')
        elif popped_node == current_node.right:
            solution.append('R')
        current_node = popped_node

    solution.append('G')
    return solution
