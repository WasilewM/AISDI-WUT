from node import Node


def get_sorted_list(root_ptr):
    sorted_list = []

    if root_ptr.left is None:
        return root_ptr.value

    if root_ptr.right is None:
        return root_ptr.value

    if root_ptr.left is not None:
        left_subtree = []
        left_subtree.append(get_sorted_list(root_ptr.left))

        for item in left_subtree:
            sorted_list.append(item)

        sorted_list.append(root_ptr.value)

    if root_ptr.right is not None:
        sorted_list.append(get_sorted_list(root_ptr.right))

    return sorted_list


def insert_new_value(root_ptr, new_value):
    if root_ptr is None:
        root_ptr = Node(new_value)
        return root_ptr

    if new_value < root_ptr.value:
        root_ptr.left = insert_new_value(root_ptr.left, new_value)
    else:
        root_ptr.right = insert_new_value(root_ptr.right, new_value)

    return root_ptr


tree = Node(10)
tree = insert_new_value(tree, 5)
tree = insert_new_value(tree, 20)
tree = insert_new_value(tree, 200)
tree = insert_new_value(tree, 1)
tree = insert_new_value(tree, 3)
tree = insert_new_value(tree, 7)
tree = insert_new_value(tree, 12)
print(get_sorted_list(tree))
