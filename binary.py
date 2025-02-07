class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search(node.left, data)
        return self._search(node.right, data)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        res = []
        if node:
            res = self._inorder(node.left)
            res.append(node.data)
            res = res + self._inorder(node.right)
        return res

# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
print(bst.inorder())  # Output: [5, 10, 20]
found_node = bst.search(10)
if found_node:
    print(f"Found: {found_node.data}")  # Output: Found: 10
