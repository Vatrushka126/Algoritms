
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def search(self, node, x):
        if node is None:
            return False

        if node.data == x:
            return True

        if x < node.data:
            return self.search(node.left, x)

        return self.search(node.right, x)

    def find_max_node(self, node):
        if node.right is None:
            return node

        return self.find_max_node(node.right)

    def insert(self, node, x):
        if node is None:
            return Node(x)

        if x < node.data:
            node.left = self.insert(node.left, x)

        elif x > node.data:
            node.right = self.insert(node.right, x)

        return node

    def add(self, x):
        if self.search(self.root, x):
            return False

        self.root = self.insert(self.root, x)
        return True

    def delete(self, node, x):
        if node is None:
            return None

        if x < node.data:
            node.left = self.delete(node.left, x)

        elif x > node.data:
            node.right = self.delete(node.right, x)

        elif node.left is not None and node.right is not None:
            node.data = self.find_max_node(node.left).data
            node.left = self.delete(node.left, node.data)

        elif node.left is not None:
            node = node.left

        elif node.right is not None:
            node = node.right

        else:
            node = None

        return node

    def remove(self, x):
        if not self.search(self.root, x):
            return False

        self.root = self.delete(self.root, x)
        return True

    def print_tree(self, node, level=0):
        if node is None:
            return

        self.print_tree(node.left, level + 1)

        print("." * level + str(node.data))

        self.print_tree(node.right, level + 1)

tree = BinaryTree()

while True:
    try:
        command = input().split()

        if not command:
            continue

        if command[0] == "ADD":
            x = int(command[1])

            if tree.add(x):
                print("DONE")
            else:
                print("ALREADY")

        elif command[0] == "DELETE":
            x = int(command[1])

            if tree.remove(x):
                print("DONE")
            else:
                print("CANNOT")

        elif command[0] == "SEARCH":
            x = int(command[1])

            if tree.search(tree.root, x):
                print("YES")
            else:
                print("NO")

        elif command[0] == "PRINTTREE":
            tree.print_tree(tree.root)

    except EOFError:
        break
