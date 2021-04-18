from new_bst import BST

tree = BST()
root = None
root = tree.insert_new_value(root, 50)
root = tree.insert_new_value(root, 30)
root = tree.insert_new_value(root, 70)
root = tree.insert_new_value(root, 20)
root = tree.insert_new_value(root, 40)
root = tree.insert_new_value(root, 60)
root = tree.insert_new_value(root, 80)
root = tree.insert_new_value(root, 5)
root = tree.insert_new_value(root, 35)
root = tree.insert_new_value(root, 55)
root = tree.insert_new_value(root, 75)
root = tree.insert_new_value(root, 85)
root = tree.insert_new_value(root, 65)
root = tree.insert_new_value(root, 45)
root = tree.insert_new_value(root, 25)

print('After creating a BST:')
tree.prepare_printable_tree(root, 'root')
tree.print_tree()

print('\n', 'After deleting 50:')
root = tree.delete_value(root, 50)
tree.clear_printable_tree()
tree.prepare_printable_tree(root, 'root')
tree.print_tree()
