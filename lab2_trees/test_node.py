from node import Node


def test_init_node_no_values():
    nd = Node(12)
    assert nd.get_value() == 12
    assert nd.get_parent() is None
    assert nd.get_left() is None
    assert nd.get_right() is None


def test_init_node_regular_node_case():
    nd = Node(12, 5, 1, 10)
    assert nd.get_value() == 12
    assert nd.get_parent() == 5
    assert nd.get_left() == 1
    assert nd.get_right() == 10


def test_init_node_root_node_case():
    nd = Node(12, left=1, right=10)
    assert nd.get_value() == 12
    assert nd.get_parent() is None
    assert nd.get_left() == 1
    assert nd.get_right() == 10


def test_init_node_leaf_node_case():
    nd = Node(12, parent=10)
    assert nd.get_value() == 12
    assert nd.get_parent() == 10
    assert nd.get_left() is None
    assert nd.get_right() is None
