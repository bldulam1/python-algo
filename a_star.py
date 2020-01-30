class Grid:
    def __init__(self, r, c):
        self.r, self.c = r, c



class Node:
    def __init__(self, r, c, parent=None):
        self.r, self.c, self.parent = r, c, parent
        self.cost = None

    def is_inside(self, grid):
        return 0 <= self.r < grid.r and 0 <= self.c < grid.c

    def is_inside_list(self, nodes_list):
        return any([neighbor.is_equal(n_c) for n_c in nodes_list])

    def is_equal(self, other_node):
        return self.r == other_node.r and self.c == other_node.c

    def neighbors(self):
        top = Node(self.r + 1, self.c, self)
        bottom = Node(self.r - 1, self.c, self)
        left = Node(self.r, self.c - 1, self)
        right = Node(self.r, self.c + 1, self)
        return top, bottom, left, right

    def __str__(self):
        return "[{},{}]".format(self.r, self.c)

    def f_cost(self, start_node, end_node):
        if self.cost is None:
            h = abs(self.r - start_node.r) + abs(self.c - start_node.c)
            g = abs(self.r - end_node.r) + abs(self.c - end_node.c)
            self.cost = h + g

        return self.cost


def get_best_node(nodes, s_node, e_node):
    best_ind = None
    best_cost = None

    for ind in range(len(nodes)):
        cost = nodes[ind].f_cost(s_node, e_node)

        if not best_cost or best_cost > cost:
            best_cost = cost
            best_ind = ind

    return best_ind


if __name__ == '__main__':
    grid = Grid(6, 11)

    start = Node(4, 7)
    end = Node(1, 4)

    blocks = [Node(1, 3), Node(2, 3), Node(2, 5), Node(2, 6), Node(2, 7)]

    open_nodes = [start]
    closed_nodes = []

    while True:
        b_ind = get_best_node(open_nodes, start, end)

        current = open_nodes.pop(b_ind)
        closed_nodes.append(current)

        if current.is_equal(end):
            c_pointer = current
            while c_pointer:
                c_pointer = c_pointer.parent
                print("Path", c_pointer)
            break

        for neighbor in current.neighbors():
            is_neighbor_traversable = neighbor.is_inside(grid) and not any([
                neighbor.is_equal(n_c) for n_c in blocks])
            is_neighbor_closed = any([neighbor.is_equal(n_c) for n_c in closed_nodes])

            if not is_neighbor_traversable or is_neighbor_closed:
                continue

            is_neighbor_in_open = any([neighbor.is_equal(n_c) for n_c in open_nodes])
            if not is_neighbor_in_open:
                open_nodes.append(neighbor)
