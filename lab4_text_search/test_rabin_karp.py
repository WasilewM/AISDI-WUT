from rabin_karp import find_rk


def test_rabin_karp_simple():
    pattern = "BBAB"
    text = "BBABBBBAB"
    assert find_rk(pattern, text) == [0, 5]


def test_rabin_karp_simple2():
    pattern = "AB"
    text = "ABBABAAB"
    assert find_rk(pattern, text) == [0, 3, 6]
