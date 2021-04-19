from avl import AVLTree
from bst import BST
from random import randint
import time

numbers_quantity = 5000
MININT = 1
MAXINT = 3 * numbers_quantity + 1
DELTA = 100


def get_random_numbers():
    geterated_numbers = []
    it = 0
    while it < numbers_quantity:
        geterated_numbers.append(randint(MININT, MAXINT))
        it += 1
    return geterated_numbers


def create_results_record(start_time, finish_time):
    current_res = str(finish_time - start_time) + ';'
    return current_res


def test_BST_performance(numbers):
    results_creating_tree = ""
    quantity = DELTA
    while quantity < len(numbers):
        tree = BST()
        root = None

        start_time = time.time()
        for num in numbers[:quantity]:
            root = tree.insert_new_value(root, num)
        finish_time = time.time()
        results_creating_tree += create_results_record(start_time, finish_time)

        quantity += DELTA

    # creating a tree for rest of the tests
    tree = BST()
    root = None
    for num in numbers:
        root = tree.insert_new_value(root, num)

    results_search_number = ""
    quantity = DELTA
    while quantity < len(numbers):
        tree = BST()
        root = None

        start_time = time.time()
        for num in numbers[:quantity]:
            root = tree.tree_search(root, num)
        finish_time = time.time()
        results_search_number += create_results_record(start_time, finish_time)

        quantity += DELTA

    result_delete_number = ""
    quantity = DELTA
    while quantity < len(numbers):
        tree = BST()
        root = None

        start_time = time.time()
        for num in numbers[:quantity]:
            root = tree.delete_value(root, num)
        finish_time = time.time()
        result_delete_number += create_results_record(start_time, finish_time)

        quantity += DELTA

    # results_creating_tree += '\n'
    # results_search_number += '\n'
    # result_delete_number += '\n'

    return [
        results_creating_tree,
        results_search_number,
        result_delete_number
    ]


def test_AVL_performance(numbers):
    results_creating_tree = ""
    quantity = DELTA
    while quantity < len(numbers):
        tree = AVLTree()
        root = None

        start_time = time.time()
        for num in numbers[:quantity]:
            root = tree.insert_new_value(root, num)
        finish_time = time.time()
        results_creating_tree += create_results_record(start_time, finish_time)

        quantity += DELTA

    # creating a tree for rest of the tests
    tree = AVLTree()
    root = None
    for num in numbers:
        root = tree.insert_new_value(root, num)

    results_search_number = ""
    quantity = DELTA
    while quantity < len(numbers):
        tree = BST()
        root = None

        start_time = time.time()
        for num in numbers[:quantity]:
            root = tree.tree_search(root, num)
        finish_time = time.time()
        results_search_number += create_results_record(start_time, finish_time)

        quantity += DELTA

    result_delete_number = ""
    quantity = DELTA
    while quantity < len(numbers):
        tree = BST()
        root = None

        start_time = time.time()
        for num in numbers[:quantity]:
            root = tree.delete_value(root, num)
        finish_time = time.time()
        result_delete_number += create_results_record(start_time, finish_time)

        quantity += DELTA

    # results_creating_tree += '\n'
    # results_search_number += '\n'
    # result_delete_number += '\n'

    return [
        results_creating_tree,
        results_search_number,
        result_delete_number
    ]
