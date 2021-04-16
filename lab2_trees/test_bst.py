from node import Node
from bst import insert_new_value


def test_bst_init():
    # tree is a pointer to root
    tree = Node(30)
    assert tree.value == 30
    assert tree.left is None
    assert tree.right is None


def test_bst_3_nodes():
    tree = Node(10)
    tree = insert_new_value(tree, 5)
    tree = insert_new_value(tree, 20)

    assert tree.left.value == 5
    assert tree.value == 10
    assert tree.right.value == 20
