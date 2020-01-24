def rotate(grid, n):
    for r in range(n):
        for c in range(r):
            grid[r][c], grid[c][r] = grid[c][r], grid[r][c]
