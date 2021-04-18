class Node:
    def __init__(self, new_value, lft=None, rght=None):
        self.value = new_value
<<<<<<< HEAD
        self.left = lft
        self.right = rght
=======
        self.left = None
        self.right = None


class NodeAVL(Node):
    def __init__(self, new_value):
        super().__init__(new_value)
        self.height = 1
>>>>>>> 2039f5ffc9a2ff8d8d098515c10345ef3e37dbb4
