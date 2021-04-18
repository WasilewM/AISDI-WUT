from node import NodeAVL


class BST:
    def __init__(self):
        self.printable_tree = dict()

    def insert_new_value(self, root, new_value):
        if root is None:
            root = NodeAVL(new_value)
            return root

        if new_value < root.value:
            root.left = self.insert_new_value(root.left, new_value)
        else:
            root.right = self.insert_new_value(root.right, new_value)

        return root

    def tree_search(self, root, look_for_val):
        if root is None:
            return root
        if look_for_val == root.value:
            return root
        if look_for_val < root.value:
            return self.tree_search(root.left, look_for_val)
        else:
            return self.tree_search(root.right, look_for_val)

    def delete_value(self, root, value_to_delete):
        if root is None:
            return root
        elif value_to_delete < root.value:
            root.left = self.delete_value(root.left, value_to_delete)
        elif value_to_delete > root.value:
            root.right = self.delete_value(root.right, value_to_delete)
        else:       # we found value to delete
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

        return root

    def get_smallest_node(self, root):
        if root is None:
            return root
        if root.left is None:
            return root
        return self.get_smallest_node(root.left)

    def prepare_printable_tree(self, node_ptr, desc, lvl=0):
        if node_ptr is not None:
            if desc == 'root':
                self.printable_tree[lvl] = []
                self.printable_tree[lvl].append((node_ptr.value, desc))

            lvl += 1
            if lvl not in self.printable_tree.keys():
                self.printable_tree[lvl] = []

            if node_ptr.left is not None:
                self.printable_tree[lvl].append(
                    (node_ptr.left.value, "came from:" + str(node_ptr.value))
                )
                self.prepare_printable_tree(node_ptr.left, node_ptr.value, lvl)

            if node_ptr.right is not None:
                self.printable_tree[lvl].append(
                    (node_ptr.right.value, "came from:" + str(node_ptr.value))
                )
                self.prepare_printable_tree(
                    node_ptr.right, node_ptr.value, lvl
                    )

    def print_tree(self):
        for key in self.printable_tree:
            if self.printable_tree[key] != []:
                print(self.printable_tree[key])

    def clear_printable_tree(self):
        it = 0
        while it in self.printable_tree.keys():
            self.printable_tree[it] = []
            it += 1
