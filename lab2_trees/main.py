from check_trees_performance import (
    get_random_numbers,
    test_AVL_performance,
    test_BST_performance
)
from model_io import save_data

test_numbers = get_random_numbers()
avl_results = test_AVL_performance(test_numbers)
bst_results = test_BST_performance(test_numbers)
save_data(avl_results, bst_results)
