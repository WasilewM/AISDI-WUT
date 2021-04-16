class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.set_value(value)
        self.set_parent(parent)
        self.set_left(left)
        self.set_right(right)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_parent(self, new_parent):
        self._parent = new_parent

    def get_parent(self):
        return self._parent

    def set_left(self, new_left):
        self._left = new_left

    def get_left(self):
        return self._left

    def set_right(self, new_right):
        self._right = new_right

    def get_right(self):
        return self._right
