from collections import defaultdict


def shortDis(n, graph, start):
    distances = [-1 for _ in range(n)]
    distances[start-1] = 0

    queue = [start]
    dis = 6
    while queue:
        new_queue = []
        for node in queue:
            for neighbor in graph[node]:
                if distances[neighbor-1] == -1:
                    distances[neighbor-1] = dis
                    new_queue.append(neighbor)

        queue = new_queue.copy()
        dis += 6

    distances.pop(start-1)

    return distances


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(value) for value in input().split()]

        graph = defaultdict(set)
        for i in range(m):
            u, v = map(int, input().strip().split())
            graph[u].add(v)
            graph[v].add(u)

        start = int(input())
        res = shortDis(n, graph, start)
        print(*res)
