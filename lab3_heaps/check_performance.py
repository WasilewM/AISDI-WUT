from heap import Heap
import random
from time import time
QUANTITY = int(1e5)
MIN_VALUE = 1
MAX_VALUE = int(3e6)
DELTA = int(1e4)


def get_random_nums_list():
    random_nums = []
    while len(random_nums) < QUANTITY:
        random_nums.append(random.randint(MIN_VALUE, MAX_VALUE))
    return random_nums


def create_results_record(start_time, finish_time):
    current_res = str(finish_time - start_time) + ';'
    return current_res


def test_heap_performance(test_nums, dimension):
    results_creating_heap = ""
    quantity = DELTA

    while quantity <= len(test_nums):
        binary_heap = Heap(dimension)

        start_t = time()
        for num in test_nums[:quantity]:
            binary_heap.add(num)
        finish_t = time()
        results_creating_heap += create_results_record(start_t, finish_t)
        quantity += DELTA

    quantity = DELTA
    results_pop_root = ""

    while quantity <= len(test_nums):
        binary_heap = Heap(dimension)
        for num in test_nums:
            binary_heap.add(num)

        start_t = time()
        for num in test_nums[:quantity]:
            binary_heap.pop()
        finish_t = time()
        results_pop_root += create_results_record(start_t, finish_t)
        quantity += DELTA

    return (results_creating_heap, results_pop_root)
