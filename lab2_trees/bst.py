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
    current = node_ptr

    while current is not None:
        current = current.right

    return current


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
        node_ptr.value = temp_ptr.value

        node_ptr.left = delete_node(node_ptr.left, temp_ptr.value)
    return node_ptr


printing_list = []


def print_tree(node_ptr):
    if node_ptr is not None:
        printing_list.append(node_ptr.value)
        if node_ptr.left is None:
            left_value = None
        else:
            left_value = node_ptr.left.value
        if node_ptr.right is None:
            right_value = None
        else:
            right_value = node_ptr.right.value

        printing_list.append(left_value)
        printing_list.append(right_value)

        print_tree(node_ptr.left)
        print_tree(node_ptr.right)


# tree = Node(50)
# tree = insert_new_value(tree, 30)
# tree = insert_new_value(tree, 70)
# tree = insert_new_value(tree, 20)
# tree = insert_new_value(tree, 40)
# tree = insert_new_value(tree, 50)
# tree = insert_new_value(tree, 80)
# tree = insert_new_value(tree, 5)
# tree = insert_new_value(tree, 35)
# tree = insert_new_value(tree, 55)
# tree = insert_new_value(tree, 75)
# tree = insert_new_value(tree, 85)
# tree = insert_new_value(tree, 65)
# tree = insert_new_value(tree, 45)
# tree = insert_new_value(tree, 25)
# # print_sorted_list(tree)
# # print(tree_search(tree, 70))
# print_tree(tree)
# print(printing_list)
