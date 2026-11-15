import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, x):
        if self.root is None:
            self.root = Node(x)
            return

        node = self.root

        while True:
            if x < node.data:
                if node.left is None:
                    node.left = Node(x)
                    return
                node = node.left

            elif x > node.data:
                if node.right is None:
                    node.right = Node(x)
                    return
                node = node.right

            else:
                return

    def count_levels(self, node):
        if node is None:
            return 0

        left = self.count_levels(node.left)
        right = self.count_levels(node.right)

        return max(left, right) + 1


tree = BinaryTree()

numbers = map(int, sys.stdin.buffer.read().split())

for x in numbers:
    if x == 0:
        break
    tree.add(x)

print(tree.count_levels(tree.root))
