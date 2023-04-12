class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)
    def bfs(self):
        res = []
        q = [self.root]
        while q:
            node = q[0]
            q = q[1:]
            res.append(str(node.data))
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
            
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    
    bst = BinarySearchTree()
    
    for val in l:
        bst.insert(val)
    
    print(f'Case {i+1}:')
    print(bst.prefix())
    print()