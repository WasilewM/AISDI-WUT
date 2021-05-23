from rabin_karp import find_rk


def test_Rabin_Karp_simple():
    find_this = "Ala"
    text_to_be_searched = "Ala ma kota."
    assert find_rk(find_this, text_to_be_searched) == [0]


def test_Rabin_Karp_single_more_difficult():
    find_this = "Ala"
    text_to_be_searched = "Bla bla bla - Ala ma kota."
    # enumerating text:    0   4   8     14
    assert find_rk(find_this, text_to_be_searched) == [14]


def test_Rabin_Karp_numerous():
    find_this = "kot"
    text_to_be_searched = "kot KOT kot KOT kot pies"
    assert find_rk(find_this, text_to_be_searched) == [0, 8, 16]


def test_Rabin_Karp_numerous_nums_in_text():
    find_this = "5"
    text_to_be_searched = "3.14159265359"
    assert find_rk(find_this, text_to_be_searched) == [5, 9, 11]


def test_Rabin_Karp_no_pattern_occurring_in_text():
    find_this = "5"
    text_to_be_searched = "BALIN"
    assert find_rk(find_this, text_to_be_searched) == []
