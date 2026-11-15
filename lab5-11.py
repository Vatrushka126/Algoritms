class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        node = self.root
        while True:
            if key == node.data:
                return
            elif key < node.data:
                if node.left is None:
                    node.left = Node(key)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(key)
                    return
                node = node.right       

    def next(self,i):
        node = self.root
        otv = -1
        while node is not None:
            if node.data >= i:
                otv = node.data
                node = node.left
            else:
                node = node.right
        return otv
        
n = int(input())     
tree = BinarySearchTree()

flag = False

for _ in range(n):
    cmd, val = input().split()
    i = int(val)

    if cmd == '+':
        if flag:
            i = (i+y) % 10**9
        tree.add(i)
        flag = False
    else:
        y = tree.next(i)
        print(y)
        flag = True