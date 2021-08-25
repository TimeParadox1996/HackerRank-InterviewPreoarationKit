def maxXor(arr, queries):
    arr = list(set(arr))
    k = len(bin(max(arr + queries))) - 2
    arr = ['{:b}'.format(x).zfill(k) for x in arr]

    trie = {}
    for number in arr:
        node = trie
        for char in number:
            node = node.setdefault(char, {})

    for q in queries:
        node = trie
        s = ''
        for char in '{:b}'.format(q).zfill(k):
            tmp = str(int(char) ^ 1)
            tmp = tmp if tmp in node else char
            s += tmp
            node = node[tmp]

        print(int(s, 2) ^ q)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    m = int(input())
    queries = []
    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    maxXor(arr, queries)

