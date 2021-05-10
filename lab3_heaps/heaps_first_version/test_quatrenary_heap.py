from quaternary_heap import Quaternary_Heap


def test_qheap_init():
    qheap = Quaternary_Heap()
    assert qheap.get_dimension() == 4
    assert qheap.heap == []


def test_qheap_add_single_value():
    qheap = Quaternary_Heap()
    qheap.add(10)
    assert qheap.heap == [-1, 10]


def test_qheap_add_multiple_values():
    qheap = Quaternary_Heap()
    qheap.add(1)
    qheap.add(100)
    qheap.add(10)
    qheap.add(16)
    qheap.add(50)
    assert qheap.heap == [-1, 100, -1, -1, 1, 10, 16, 50]
    assert qheap.next_value_index() == 16


def test_qheap_delete_root():
    qheap = Quaternary_Heap()
    qheap.add(1)
    qheap.add(100)
    qheap.add(10)
    assert qheap.heap == [-1, 100, -1, -1, 1, 10]
    assert qheap.next_value_index() == 6
    qheap.delete_root()
    assert qheap.next_value_index() == 5


def test_qheap_delete_root_multiple_times():
    qheap = Quaternary_Heap()
    qheap.add(1)
    qheap.add(10)
    qheap.add(20)
    qheap.add(30)
    qheap.add(40)
    qheap.add(100)

    correct_answer = [-1, 100, -1, -1, 40, 10, 20, 30]
    while len(correct_answer) < 17:
        correct_answer.append(-1)
    correct_answer[16] = 1

    assert qheap.heap == correct_answer
    assert qheap.next_value_index() == 17
    qheap.delete_root()
    assert qheap.next_value_index() == 16
    qheap.delete_root()
    assert qheap.next_value_index() == 7
