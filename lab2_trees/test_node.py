from node import Node


def test_init_single_node():
    nd = Node(12)
    assert nd.value == 12
    assert nd.left is None
    assert nd.right is None


def test_init_multiple_nodes():
    nd = Node(2)
    nd2 = Node(13)
    root = Node(10)
    root.left = nd
    root.right = nd2
    assert root.value == 10
    assert root.left == nd
    assert root.left.value == 2
    assert root.right == nd2
    assert root.right.value == 13
