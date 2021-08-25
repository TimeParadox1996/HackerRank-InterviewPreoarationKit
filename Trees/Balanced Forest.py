class Node:
    def __init__(self, index, value):
        self.parent = None
        self.index = index
        self.value = value
        self.children = []


class Tree:
    def __init__(self, n):
        self.nodes = [Node(i, i) for i in range(n)]

    def add_child(self, index, value, children):
        self.nodes[index].value = value
        self.nodes[index].children = children
        for c in children:
            self.nodes[c].parent = index
        

def balancedForest(n, c, graph):
    costs = [0 for _ in range(n)]

    def find_costs(start):
        cost = c[start]
        for child in graph[start]:
            cost += find_costs(child)

        costs[start] = cost
        return cost

    t_cost = find_costs(0)

    minimum = t_cost // 3
    if t_cost % 3 > 0:
        minimum += 1

    maximum = t_cost // 2

    for x in range(n):
        if minimum <= c[x] <= maximum:
            remain = t_cost - c[x]






    return 0


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())
        c = list(map(int, input().rstrip().split()))

        graph = [[] for _ in range(n)]
        for _ in range(n - 1):
            a, b = map(int, input().rstrip().split())
            a, b = min(a, b)-1, max(a, b)-1
            graph[a].append(b)

        result = balancedForest(n, c, graph)
        #print(result)
