from node import Node

sorted_list = []


def get_sorted_list(node_ptr):
    if node_ptr:
        get_sorted_list(node_ptr.left)
        sorted_list.append(node_ptr.value)
        get_sorted_list(node_ptr.right)


def insert_new_value(node_ptr, new_value):
    if node_ptr is None:
        node_ptr = Node(new_value)
        return node_ptr

    if new_value < node_ptr.value:
        node_ptr.left = insert_new_value(node_ptr.left, new_value)
    else:
        node_ptr.right = insert_new_value(node_ptr.right, new_value)

    return node_ptr


def tree_search(node_ptr, look_for_val):
    if node_ptr is None:
        return node_ptr
    if look_for_val == node_ptr.value:
        return node_ptr
    if look_for_val < node_ptr.value:
        return tree_search(node_ptr.left, look_for_val)
    else:
        return tree_search(node_ptr.right, look_for_val)
