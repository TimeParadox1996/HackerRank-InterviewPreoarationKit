class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def lca(root, v1, v2):
    paths = [[root]]
    path1 = []
    path2 = []

    if v1 == root.info:
        path1 = [root]
    if v2 == root.info:
        path2 = [root]

    while paths:
        new_paths = []
        for path in paths:
            last_node = path[-1]
            if last_node.left is not None:
                if last_node.left.info == v1:
                    path1 = path + [last_node.left]
                elif last_node.left.info == v2:
                    path2 = path + [last_node.left]
                new_paths.append(path + [last_node.left])
            if last_node.right is not None:
                if last_node.right.info == v1:
                    path1 = path + [last_node.right]
                elif last_node.right.info == v2:
                    path2 = path + [last_node.right]
                new_paths.append(path + [last_node.right])

        paths = new_paths.copy()

    common = 0
    for i in range(min(len(path1), len(path2))):
        if path1[i].info == path2[i].info:
            common = path1[i]
        else:
            break

    return common


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
