def get_neighbors(r, c, rs, cs):
    neighbors = []
    for ri in r - 1, r, r + 1:
        for ci in c - 1, c, c + 1:
            if 0 <= ri < rs and 0 <= ci < cs and not (ri == r and ci == c):
                neighbors.append((ri, ci))

    return neighbors


def mine_sweeper(bombs, num_rows, num_cols):
    grid = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for r, c in bombs:
        grid[r][c] = -1
        for rn, cn in get_neighbors(r, c, num_rows, num_cols):
            if grid[rn][cn] >= 0:
                grid[rn][cn] += 1

    return grid


def reveal(grid, r, c):
    queue = [(r, c)]
    rs, cs = len(grid), len(grid[0])

    while len(queue):
        rf, cf = queue.pop(0)
        if grid[rf][cf] == 0:
            grid[rf][cf] = -2

            queue += get_neighbors(rf, cf, rs, cs)
