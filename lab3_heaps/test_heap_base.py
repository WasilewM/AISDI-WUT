from heap_base import Heap_Base


def test_init_default():
    examplary_heap = Heap_Base()
    assert examplary_heap.get_dimension() == 2
    assert examplary_heap.heap == []
    assert examplary_heap.next_value_index() == 1


def test_init_given_dimension():
    examplary_heap = Heap_Base(4)
    assert examplary_heap.get_dimension() == 4
    assert examplary_heap.heap == []
    assert examplary_heap.next_value_index() == 1


def test_init_given_dimension_less_then_2():
    examplary_heap = Heap_Base(1)
    assert examplary_heap.get_dimension() == 2
    assert examplary_heap.heap == []


def test_extend_heap_list():
    examplary_heap = Heap_Base()
    assert examplary_heap.heap == []

    examplary_heap.extend_heap_list(10)
    correct_heap_list = [-1 for _ in range(11)]
    assert examplary_heap.heap == correct_heap_list
