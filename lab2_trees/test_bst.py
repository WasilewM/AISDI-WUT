from node import Node
from bst import (
    insert_new_value,
    sorted_list,
    get_sorted_list,
    tree_search
)


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


def test_get_sorted_list():
    tree = Node(10)
    tree = insert_new_value(tree, 5)
    tree = insert_new_value(tree, 20)
    tree = insert_new_value(tree, 200)
    tree = insert_new_value(tree, 1)
    tree = insert_new_value(tree, 3)
    tree = insert_new_value(tree, 7)
    tree = insert_new_value(tree, 12)
    get_sorted_list(tree)
    assert sorted_list == [1, 3, 5, 7, 10, 12, 20, 200]


def test_tree_search_node_exists():
    tree = Node(10)
    tree = insert_new_value(tree, 5)
    tree = insert_new_value(tree, 20)
    tree = insert_new_value(tree, 200)
    tree = insert_new_value(tree, 1)
    tree = insert_new_value(tree, 3)
    tree = insert_new_value(tree, 7)
    tree = insert_new_value(tree, 12)
    nd = tree_search(tree, 20)

    assert nd.value == 20
    assert nd.left.value == 12
    assert nd.right.value == 200


def test_tree_search_node_does_not_exist():
    tree = Node(10)
    tree = insert_new_value(tree, 5)
    tree = insert_new_value(tree, 20)
    tree = insert_new_value(tree, 200)
    tree = insert_new_value(tree, 1)
    tree = insert_new_value(tree, 3)
    tree = insert_new_value(tree, 7)
    tree = insert_new_value(tree, 12)
    nd = tree_search(tree, 210)

    assert nd is None
