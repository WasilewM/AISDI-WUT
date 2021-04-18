class Node:
    def __init__(self, new_value, lft=None, rght=None):
        self.value = new_value
        self.left = lft
        self.right = rght


class NodeAVL(Node):
    def __init__(self, new_value):
        super().__init__(new_value)
        self.height = 1
