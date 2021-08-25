def maxRegion(n, m, grid):
    filled_cells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                filled_cells.append((i, j))

    max_region = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    while filled_cells:
        first = filled_cells.pop()
        queue = [first]
        visited[first[0]][first[1]] = True
        count = 1
        while queue:
            cell = queue.pop()
            for x in range(max(cell[0]-1, 0), min(cell[0]+2, n)):
                for y in range(max(cell[1]-1, 0), min(cell[1]+2, m)):
                    if not visited[x][y] and grid[x][y] == 1:
                        visited[x][y] = True
                        queue.append((x, y))
                        filled_cells.remove((x, y))
                        count += 1

        max_region = max(max_region, count)

    return max_region


if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())

    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(n, m, grid)
    print(res)
