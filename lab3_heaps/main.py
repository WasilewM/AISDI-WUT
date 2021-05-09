from check_performance import (
    get_random_nums_list,
    test_heap_performance,
    # test_quaternary_heap_performance
)
from model_io import save_data

test_nums = get_random_nums_list()
b_heap = test_heap_performance(test_nums, 2)
t_heap = test_heap_performance(test_nums, 3)
q_heap = test_heap_performance(test_nums, 4)
# q_heap_v1 = test_quaternary_heap_performance(test_nums)

save_data(b_heap, t_heap, q_heap)
