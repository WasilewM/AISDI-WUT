from avl import AVLTree

tree = AVLTree()
root = None

root = tree.insert_new_value(root, 5)
root = tree.insert_new_value(root, 30)
root = tree.insert_new_value(root, 7)
root = tree.insert_new_value(root, 20)
root = tree.insert_new_value(root, 440)
root = tree.insert_new_value(root, 60)
root = tree.insert_new_value(root, 18)
root = tree.insert_new_value(root, 5)
root = tree.insert_new_value(root, 63)
root = tree.insert_new_value(root, 550)
root = tree.insert_new_value(root, 75)
root = tree.insert_new_value(root, 85)
root = tree.insert_new_value(root, 65)
root = tree.insert_new_value(root, 45)
root = tree.insert_new_value(root, 25)

print('After creating a AVL:')
tree.prepare_printable_tree(root, 'root')
tree.print_tree()
