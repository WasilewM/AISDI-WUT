from bucket_sort import bucket_sort


def test_bucket_sort_typical_mixed_chars():
    table = ['!', 'Q', 'A', 'Z', '2', 'w', 's', 'x']
    assert bucket_sort(table) == sorted(table)


def test_backet_sort_oposite_order():
    table = ['8', '7', '5', '4', '3', '1']
    assert bucket_sort(table) == sorted(table)


def test_backet_sort_only_ones():
    table = ['1', '1', '1', '1']
    assert bucket_sort(table) == sorted(table)
