from merge_sort import merge_sort


def test_merge_sort():
    table = ['!', 'Q', 'A', 'Z', '2', 'w', 's', 'x']
    sorted_table = sorted(table)
    assert merge_sort(table) == sorted_table


def test_merge_sort_oposite_order():
    table = ['8', '7', '5', '4', '3', '1']
    assert merge_sort(table) == sorted(table)


def test_merge_sort_only_ones():
    table = ['1', '1', '1', '1']
    assert merge_sort(table) == sorted(table)
