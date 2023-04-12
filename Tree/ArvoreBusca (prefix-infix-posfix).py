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
            
    def prefix(self):
        result = []
        self._prefix(self.root, result)
        return result
    def _prefix(self, node, result):
        if node != None:
            result.append(str(node.data))
            self._prefix(node.left, result)
            self._prefix(node.right, result)
            
    def infix(self):
        result = []
        self._infix(self.root, result)
        return result

    def _infix(self, node, result):
        if node is not None:
            self._infix(node.left, result)
            result.append(str(node.data))
            self._infix(node.right, result)

    def posfix(self):
        result = []
        self._posfix(self.root, result)
        return result

    def _posfix(self, node, result):
        if node is not None:
            self._posfix(node.left, result)
            self._posfix(node.right, result)
            result.append(str(node.data))
            
        
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    
    bst = BinarySearchTree()
    
    for val in l:
        bst.insert(val)
    
    print(f'Case {i+1}:')
    print(f'Pre.: {" ".join(bst.prefix())}')
    print(f'In..: {" ".join(bst.infix())}')
    print(f'Post: {" ".join(bst.posfix())}')
    print()
