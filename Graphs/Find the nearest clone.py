from collections import defaultdict, deque


def findShortest(n, graph, colors, sel_color):
    queue = deque()
    length = [-1] * n
    visited = [False] * n

    for i in range(n):
        if colors[i] == sel_color:
            length[i] = 0
            queue.appendleft(i+1)

    while queue:
        v = queue.pop()
        visited[v-1] = True

        for u in graph[v]:
            if not visited[u-1]:
                if length[u-1] != -1:
                    return length[v-1] + length[u-1] + 1
                else:
                    length[u-1] = length[v-1] + 1
                    queue.appendleft(u)

    return -1


if __name__ == '__main__':
    graph_nodes, graph_edges = map(int, input().split())

    graph = defaultdict(set)

    for i in range(graph_edges):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)

    colors = list(map(int, input().strip().split()))

    sel_color = int(input().strip())

    ans = findShortest(graph_nodes, graph, colors, sel_color)
    print(ans)
