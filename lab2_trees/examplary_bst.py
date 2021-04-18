from bst import (
    insert_new_value,
    delete_node,
    prepare_printable_tree,
    print_tree,
    clear_printable_tree
)
from node import Node

tree = Node(50)
tree = insert_new_value(tree, 30)
tree = insert_new_value(tree, 70)
tree = insert_new_value(tree, 20)
tree = insert_new_value(tree, 40)
tree = insert_new_value(tree, 60)
tree = insert_new_value(tree, 80)
tree = insert_new_value(tree, 5)
tree = insert_new_value(tree, 35)
tree = insert_new_value(tree, 55)
tree = insert_new_value(tree, 75)
tree = insert_new_value(tree, 85)
tree = insert_new_value(tree, 65)
tree = insert_new_value(tree, 45)
tree = insert_new_value(tree, 25)
# print_sorted_list(tree)
# print(tree_search(tree, 70))
prepare_printable_tree(tree, 'root', 0)
print_tree()

print('\n', 'After deleting 50:')
tree = delete_node(tree, 50)
clear_printable_tree()
prepare_printable_tree(tree, 'root', 0)
print_tree()

print('\n', 'After deleting 45:')
tree = delete_node(tree, 45)
clear_printable_tree()
prepare_printable_tree(tree, 'root', 0)
print_tree()
