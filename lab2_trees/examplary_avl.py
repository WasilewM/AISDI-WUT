from avl import AVLTree

Tree = AVLTree()
root = None

root = Tree.insert_new_value(root, 4)
Tree.clear_printable_tree()
Tree.prepare_printable_tree(root)
Tree.print_tree()
print()

root = Tree.insert_new_value(root, 2)
Tree.clear_printable_tree()
Tree.prepare_printable_tree(root)
Tree.print_tree()
print()

root = Tree.insert_new_value(root, 6)
Tree.clear_printable_tree()
Tree.prepare_printable_tree(root)
Tree.print_tree()
print()

root = Tree.insert_new_value(root, 1)
Tree.clear_printable_tree()
Tree.prepare_printable_tree(root)
Tree.print_tree()
print()

root = Tree.insert_new_value(root, 3)
Tree.clear_printable_tree()
Tree.prepare_printable_tree(root)
Tree.print_tree()
print()

root = Tree.insert_new_value(root, 5)
Tree.clear_printable_tree()
Tree.prepare_printable_tree(root)
Tree.print_tree()
print()

# print('After creating an AVL tree:')
# Tree.prepare_printable_tree(root)
# Tree.print_tree()
# Tree.print(root)

# print('\n', 'After deleting 4:')
# root = Tree.delete_value_AVL(root, 4)
# Tree.clear_printable_tree()
# Tree.prepare_printable_tree(root)
# Tree.print_tree()
# Tree.print(root)
