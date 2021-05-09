from heap import Heap


def test_create_heap_2():
    h2 = Heap(2)
    h2.add(1)
    h2.add(2)
    h2.add(3)
    h2.add(4)
    h2.add(6)
    h2.add(7)
    h2.add(10)

    assert h2.get_heap() == [10, 4, 7, 1, 3, 2, 6]


def test_create_heap_3():
    h3 = Heap(3)
    h3.add(1)
    h3.add(2)
    h3.add(3)
    h3.add(4)
    h3.add(6)
    h3.add(7)
    h3.add(10)

    assert h3.get_heap() == [10, 7, 2, 3, 1, 4, 6]


def test_create_heap_4():
    h4 = Heap(4)
    h4.add(1)
    h4.add(2)
    h4.add(3)
    h4.add(4)
    h4.add(6)
    h4.add(7)
    h4.add(10)

    assert h4.get_heap() == [10, 7, 2, 3, 4, 1, 6]


def test_pop_from_heap_2():
    h2 = Heap(2)
    h2.add(1)
    h2.add(2)
    h2.add(3)
    h2.add(4)
    h2.add(6)
    h2.add(7)
    h2.add(10)

    h2.pop()

    assert h2.get_heap() == [7, 4, 6, 1, 3, 2]


def test_pop_from_heap_3():
    h3 = Heap(3)
    h3.add(1)
    h3.add(2)
    h3.add(3)
    h3.add(4)
    h3.add(6)
    h3.add(7)
    h3.add(10)

    h3.pop()

    assert h3.get_heap() == [7, 6, 2, 3, 1, 4]


def test_pop_from_heap_4():
    h4 = Heap(4)
    h4.add(1)
    h4.add(2)
    h4.add(3)
    h4.add(4)
    h4.add(6)
    h4.add(7)
    h4.add(10)

    h4.pop()

    assert h4.get_heap() == [7, 6, 2, 3, 4, 1]
