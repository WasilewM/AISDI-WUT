from bubble_sort import bubble_sort


def test_bubble_sort_typical():
    my_list = [34, 10, 1, 5, 84, 47, 79]
    assert bubble_sort(my_list) == [1, 5, 10, 34, 47, 79, 84]


def test_bubble_sort_oposite_order():
    my_list = [84, 79, 47, 34, 10, 5, 1]
    assert bubble_sort(my_list) == [1, 5, 10, 34, 47, 79, 84]