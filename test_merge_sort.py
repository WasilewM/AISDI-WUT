from merge_sort import merge_sort


def test_merge_sort():
    table = ['!', 'Q', 'A', 'Z', '2', 'w', 's', 'x']
    sorted_table = sorted(table)
    assert merge_sort(table) == sorted_table
