def crosswordPuzzle(crossword, words):
    hor_spaces = []
    ver_spaces = []
    for i in range(10):
        start = -1
        end = -1
        state = False
        for j in range(10):
            if crossword[i][j] == "-":
                if state:
                    end = j+1
                else:
                    start = j
                    end = j+1
                    state = True
            else:
                if start != end:
                    hor_spaces.append([(i, start), (i, end)])
                    start = end = j
                state = False

        if state:
            hor_spaces.append([(i, start), (i, end)])

    for j in range(10):
        start = -1
        end = -1
        state = False
        for i in range(10):
            if crossword[i][j] == "-":
                if state:
                    end = i + 1
                else:
                    start = i
                    end = i + 1
                    state = True
            else:
                if start != end:
                    ver_spaces.append([(start, j), (end, j)])
                    start = end = i
                state = False

        if state:
            ver_spaces.append([(start, j), (end, j)])

    paths = [crossword]
    for word in words:
        new_paths = []
        for path in paths:
            length = len(word)
            for space in hor_spaces:
                if space[1][1] - space[0][1] == length:
                    grid = string_to_list(path)
                    start = space[0]
                    state = True
                    for y in range(len(word)):
                        if grid[start[0]][y+start[1]] == "-" or grid[start[0]][y+start[1]] == word[y]:
                            grid[start[0]][y+start[1]] = word[y]
                        else:
                            state = False
                            break

                    if state:
                        new_paths.append(list_to_string(grid))

            for space in ver_spaces:
                if space[1][0] - space[0][0] == length:
                    grid = string_to_list(path)
                    start = space[0]
                    state = True
                    for x in range(len(word)):
                        if grid[x+start[0]][start[1]] == "-" or grid[x+start[0]][start[1]] == word[x]:
                            grid[x+start[0]][start[1]] = word[x]
                        else:
                            state = False
                            break

                    if state:
                        new_paths.append(list_to_string(grid))

        paths = new_paths.copy()

    return paths[0]


def string_to_list(grid):
    new_grid = []
    for row in grid:
        new_grid.append(list(row))

    return new_grid


def list_to_string(grid):
    new_grid = []
    for row in grid:
        new_grid.append("".join(row))

    return new_grid


if __name__ == '__main__':
    crossword = []
    for _ in range(10):
        crossword_item = input().strip()
        crossword.append(crossword_item)

    words = input().strip().split(";")

    result = crosswordPuzzle(crossword, words)
    for line in result:
        print(line)


