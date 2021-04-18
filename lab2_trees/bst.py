from node import Node


def print_sorted_list(node_ptr):
    if node_ptr is not None:
        print_sorted_list(node_ptr.left)
        print(node_ptr.value)
        print_sorted_list(node_ptr.right)


def insert_new_value(node_ptr, new_value):
    if node_ptr is None:
        node_ptr = Node(new_value)
        return node_ptr

    if new_value < node_ptr.value:
        node_ptr.left = insert_new_value(node_ptr.left, new_value)
    else:
        node_ptr.right = insert_new_value(node_ptr.right, new_value)

    return node_ptr


def find_max_value_node_in_subtree(node_ptr):
    """
    Receives pointer to left subtree and finds the node with max
    value in this subtree.
    """
    current_node = node_ptr
    prev_node = None

    while current_node is not None:
        if current_node.value is not None:
            prev_node = current_node
            current_node = current_node.right
        else:
            break

    return prev_node


def tree_search(node_ptr, look_for_val):
    if node_ptr is None:
        return None

    if node_ptr is None:
        return node_ptr
    if look_for_val == node_ptr.value:
        return node_ptr
    if look_for_val < node_ptr.value:
        return tree_search(node_ptr.left, look_for_val)
    else:
        return tree_search(node_ptr.right, look_for_val)


def delete_node(node_ptr, to_be_deleted):
    if node_ptr is None:
        return None

    if to_be_deleted < node_ptr.value:
        return delete_node(node_ptr.left, to_be_deleted)
    elif to_be_deleted > node_ptr.value:
        return delete_node(node_ptr.right, to_be_deleted)
    else:
        if node_ptr.left is None:
            temp_ptr = node_ptr.right
            node_ptr = None
            return temp_ptr
        elif node_ptr.right is None:
            temp_ptr = node_ptr.left
            node_ptr = None
            return temp_ptr

        temp_ptr = find_max_value_node_in_subtree(node_ptr.left)
        node_ptr = Node(temp_ptr.value, node_ptr.left, node_ptr.right)
        temp_ptr.value = None
    return node_ptr


printable_tree = dict()


def prepare_printable_tree(node_ptr, desc, lvl):
    if node_ptr is not None:
        if desc == 'root':
            printable_tree[lvl] = []
            printable_tree[lvl].append((node_ptr.value, desc))

        lvl += 1
        if lvl not in printable_tree.keys():
            printable_tree[lvl] = []

        if node_ptr.left is not None:
            printable_tree[lvl].append(
                (node_ptr.left.value, "came from:" + str(node_ptr.value))
            )
            prepare_printable_tree(node_ptr.left, node_ptr.value, lvl)

        if node_ptr.right is not None:
            printable_tree[lvl].append(
                (node_ptr.right.value, "came from:" + str(node_ptr.value))
            )
            prepare_printable_tree(node_ptr.right, node_ptr.value, lvl)


def print_tree():
    for key in printable_tree:
        if printable_tree[key] != []:
            print(printable_tree[key])


def clear_printable_tree():
    it = 0
    while it in printable_tree.keys():
        printable_tree[it] = []
        it += 1
