from kmp import find_kmp
from naive import find_naive
from rabin_karp import find_rk


def test_empty_text():
    text = ""
    pattern = "AB"
    assert find_kmp(pattern, text) == []
    assert find_naive(pattern, text) == []
    assert find_rk(pattern, text) == []


def test_empty_pattern():
    text = "ABABA"
    pattern = ""
    assert find_kmp(pattern, text) == []
    assert find_naive(pattern, text) == []
    assert find_rk(pattern, text) == []


def test_single_pattern_occurring():
    text = "ABBABABBBBBBBAAB"
    pattern = "BABAB"
    assert find_kmp(pattern, text) == [2]
    assert find_naive(pattern, text) == [2]
    assert find_rk(pattern, text) == [2]


def test_lutliple_pattern_occurring():
    text = "ABBABABBABABBBBBBBAAB"
    pattern = "BABAB"
    assert find_kmp(pattern, text) == [2, 7]
    assert find_naive(pattern, text) == [2, 7]
    assert find_rk(pattern, text) == [2, 7]
