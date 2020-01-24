from mine_sweeper import mine_sweeper, reveal

if __name__ == '__main__':
    grid = mine_sweeper([[0, 0], [3, 3]], 4, 4)
    print(grid)
    reveal(grid, 1, 2)
    print(grid)
