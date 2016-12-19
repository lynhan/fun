def battleship(grid):
    def get_unvisited():
        unvisited = set([])
        for r in len(grid):
            for c in len(grid):
                unvisited.add((r, c))
        return unvisited

    def get_neighbors(r, c):
        neighbors = [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]
        in_grid = lambda cd: return 0 <= cd[0] < len(grid) and 0 <= cd[1] < len(grid)
        not_visited = lambda cd: return cd in unvisited
        return filter(not_visited, (filter(in_grid, neighbors)))

    mark_count = 0
    def mark():
        mark_count += 1
        if mark_count == 25:  # hard coded random num here
            print("WON")
            return

    unvisited = get_unvisited()
    def find(r, c):
        if grid[r][c]:
            mark()
            neighbors = get_neighbors(r, c)
            for cell in neighbors:
                find(cell[0], cell[1])

    while unvisited:
        cell = unvisited.pop()
        find(cell)
