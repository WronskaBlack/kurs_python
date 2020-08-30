class Node:
    def __init__(
            self,
            key: int = None,
            left: "Node" = None,
            right: "Node" = None
    ):
        self.key = key
        self.left = left
        self.right = right

    def append(self, key: int) -> None:
        if self.key is None:
            self.key = key
            return
        if key < self.key:
            # left sub-tree
            if self.left is None:
                self.left = Node(key=key)
            else:
                self.left.append(key)
        else:
            # right sub-tree
            if self.right is None:
                self.right = Node(key=key)
            else:
                self.right.append(key)

    def __repr__(self):
        return f"Node({self.key})"

    def traverse(self):
        print(self)
        if self.left is not None:
            self.left.traverse()
        if self.right is not None:
            self.right.traverse()


def traverse(root: Node):
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return result


def create_tree(root: Node, keys: list) -> Node:
    keys.sort()
    size = len(keys)
    if size:
        middle = size // 2
        root.append(keys[middle])
        create_tree(root, keys[:middle])
        create_tree(root, keys[middle + 1:])
    return root


if __name__ == "__main__":
    root = Node(10)
    root.append(8)
    root.append(6)
    root.append(5)
    root.append(3)
    root.append(12)
    root.traverse()
    print(traverse(root))
    keys = [42, 43, 45, 54, 63, 23, 43]
    root = create_tree(Node(), keys)
    print(traverse(root))