import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.count = 1
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
                node.count += 1
                return

    def print_tree(self, node):
        if node is None:
            return

        self.print_tree(node.left)
        print(node.data, node.count)
        self.print_tree(node.right)


tree = BinaryTree()

numbers = map(int, sys.stdin.buffer.read().split())

for x in numbers:
    if x == 0:
        break
    tree.add(x)

tree.print_tree(tree.root)