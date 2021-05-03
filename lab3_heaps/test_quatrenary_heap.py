from quaternary_heap import Quaternary_Heap


def test_qheap_init():
    qheap = Quaternary_Heap()
    assert qheap.get_dimension() == 4
    assert qheap.heap == []
    # assert qheap.last() == 0


def test_qheap_add_single_value():
    qheap = Quaternary_Heap()
    qheap.add(10)
    assert qheap.heap == [None, 10]
    # assert qheap.last() == 1


def test_qheap_add_multiple_values():
    qheap = Quaternary_Heap()
    qheap.add(1)
    qheap.add(100)
    qheap.add(10)
    assert qheap.heap == [None, 100, None, None, 1, 10]
    # assert qheap.last() == 5
    assert qheap.next_value_index() == 6
