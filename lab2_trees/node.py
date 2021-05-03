class Node:
    def __init__(self, new_value):
        self.value = new_value
        self.left = None
        self.right = None


class NodeAVL(Node):
    def __init__(self, new_value):
        super().__init__(new_value)
        self.height = 1
