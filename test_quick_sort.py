from quick_sort import quick_sort


def test_quick_sort_typical():
    my_list = [34, 10, 1, 5, 84, 47, 79]
    assert quick_sort(my_list) == [1, 5, 10, 34, 47, 79, 84]


def test_quick_sort_oposite_order():
    my_list = [84, 79, 47, 34, 10, 5, 1]
    assert quick_sort(my_list) == [1, 5, 10, 34, 47, 79, 84]


def test_bucket_sort_typical_mixed_chars():
    table = ['!', 'Q', 'A', 'Z', '2', 'w', 's', 'x']
    assert quick_sort(table) == sorted(table)
