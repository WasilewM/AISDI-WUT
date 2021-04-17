from node import NodeAVL

class AVLTree:
    def insert_new_value(self, node_ptr, new_value):
        if node_ptr is None:
            node_ptr = NodeAVL(new_value)
            return node_ptr

        if new_value < node_ptr.value:
            node_ptr.left = self.insert_new_value(node_ptr.left, new_value)
        else:
            node_ptr.right = self.insert_new_value(node_ptr.right, new_value)

        node_ptr.height = self.update_height(node_ptr)
        balance = self.get_balance(node_ptr)

        if balance == 2:
            if new_value < node_ptr.left.value: # Left left
                return self.rotate_right(node_ptr)
            else: # Left Right
                node_ptr.left = self.rotate_left(node_ptr.left)
                return self.rotate_right(node_ptr)

        if balance == -2:
            if new_value > node_ptr.left.value: # Right right
                return self.rotate_left(node_ptr)
            else: # Right Right
                node_ptr.right = self.rotate_right(node_ptr.right)
                return self.rotate_left(node_ptr)
        return node_ptr

    def tree_search(self, node_ptr, look_for_val):
        if node_ptr is None:
            return node_ptr
        if look_for_val == node_ptr.value:
            return node_ptr
        if look_for_val < node_ptr.value:
            return tree_search(node_ptr.left, look_for_val)
        else:
            return tree_search(node_ptr.right, look_for_val)

    def get_height(self, node_ptr):
        return 0 if not node_ptr else node_ptr.height

    def get_balance(self, node_ptr):
        return 0 if not node_ptr else self.get_height(node_ptr.left) - self.get_height(node_ptr.right)

    def rotate_left(self, root):
        pivot = root.right
        b = pivot.left
        pivot.left = root
        root.right = b

        root.height = self.update_height(root)
        pivot.height = self.update_height(pivot)
        return pivot

    def rotate_right(self, root):
        pivot = root.left
        b = pivot.right
        pivot.right = root
        root.left = b

        root.height = self.update_height(root)
        pivot.height = self.update_height(pivot)
        return pivot

    def update_height(self, node_ptr):
        return self.get_height(node_ptr.left) + 1 if node_ptr.left > node_ptr.right else node_ptr.right + 1
