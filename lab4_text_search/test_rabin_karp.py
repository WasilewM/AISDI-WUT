from rabin_karp import find_rk


def test_rabin_karp_simple():
    pattern = "CBBAB"
    text = "CBBABBCBBAB"
    assert find_rk(pattern, text) == [0, 6]


def test_rabin_karp_simple2():
    pattern = "CBBCB"
    text = "CBBCBBCBBAB"
    assert find_rk(pattern, text) == [0, 3]
