from node import NodeAVL

class AVLTree:
    def insert_new_value(self, root, new_value):
        if root is None:
            root = NodeAVL(new_value)
            return root

        if new_value < root.value:
            root.left = self.insert_new_value(root.left, new_value)
        else:
            root.right = self.insert_new_value(root.right, new_value)

        root.height = self.update_height(root)
        balance = self.get_balance(root)

        if balance == 2:
            if new_value < root.left.value: # Left left
                return self.rotate_right(root)
            else: # Left Right
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance == -2:
            if new_value > root.right.value: # Right right
                return self.rotate_left(root)
            else: # Right Right
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
        return root

    def tree_search(self, root, look_for_val):
        if root is None:
            return root
        if look_for_val == root.value:
            return root
        if look_for_val < root.value:
            return tree_search(root.left, look_for_val)
        else:
            return tree_search(root.right, look_for_val)

    def get_height(self, root):
        return 0 if not root else root.height

    def get_balance(self, root):
        return 0 if not root else self.get_height(root.left) - self.get_height(root.right)

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

    def update_height(self, root):
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def delete_value(self, root, value_to_delete):
        if root is None:
            return root
        elif value_to_delete < root.value:
            root.left = self.delete_value(root.left, value_to_delete)
        elif value_to_delete > root.value:
            root.right = self.delete_value(root.right, value_to_delete)
        else: # we found value to delete
            if root.right is None:
                temp = root.left
                root = None
                return temp
            elif root.left is None:
                temp = root.right
                root = None
                return temp
            temp = self.get_smallest_node(root.right)
            root.value = temp.value
            root.right = self.delete_value(root.right, temp.value)

        root.height = self.update_height(root)
        balance = self.get_balance(root)

        if balance == 2:
            if self.get_balance(root.left) >= 0: # Left left
                return self.rotate_right(root)
            else: # Left Right
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance == -2:
            if self.get_balance(root.right) >= 0: # Right right
                return self.rotate_left(root)
            else: # Right Right
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
        return root

    def get_smallest_node(self, root):
        if root is None:
            return root
        if root.left is None:
            return root
        return self.get_smallest_node(root.left)
    
    def print(self, root):
        if root:
            print(f"{root.value} ", end="")
            self.print(root.left)
            self.print(root.right)

Tree = AVLTree()
root = None
 
root = Tree.insert_new_value(root, 1)
root = Tree.insert_new_value(root, 2)
root = Tree.insert_new_value(root, 3)
root = Tree.insert_new_value(root, 4)
root = Tree.insert_new_value(root, 5)
root = Tree.insert_new_value(root, 6)

myTree.print(root)
print("")

root = myTree.delete_value(root, 4)
myTree.print(root)
print("")
