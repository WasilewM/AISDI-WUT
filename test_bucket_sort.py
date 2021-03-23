from bucket_sort import bucket_sort


def test_bucket_sort():
    table = ['!', 'Q', 'A', 'Z', '2', 'w', 's', 'x']
    sorted_table = sorted(table)
    assert bucket_sort(table) == sorted_table
