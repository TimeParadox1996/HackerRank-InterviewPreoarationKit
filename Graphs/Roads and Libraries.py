def roadsAndLibraries(n, m, c_lib, c_road):
    if c_lib > c_road:
        bubbles = []
        visited = set()
        for _ in range(m):
            road = set(map(int, input().rstrip().split()))
            if visited.intersection(road):
                connections = []
                for i in range(len(bubbles)):
                    if bubbles[i].intersection(road):
                        connections.append(i)

                if len(connections) == 1:
                    bubbles[connections[0]] = bubbles[connections[0]].union(road)
                    visited = visited.union(road)
                else:
                    bubbles[connections[0]] = bubbles[connections[0]].union(bubbles[connections[1]])
                    bubbles.pop(connections[1])
            else:
                bubbles.append(road)
                visited = visited.union(road)

        cost = 0
        for bubble in bubbles:
            cost += (c_lib + (len(bubble)-1) * c_road)

        not_visited = set([i for i in range(1, n+1)]) - visited
        cost += len(not_visited) * c_lib

        return cost
    else:
        for _ in range(m):
            a, b = map(int, input().rstrip().split())

        return n * c_lib


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n, m, c_lib, c_road = map(int, input().strip().split())

        result = roadsAndLibraries(n, m, c_lib, c_road)
        print(result)
