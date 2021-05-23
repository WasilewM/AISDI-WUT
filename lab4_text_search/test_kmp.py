from kmp import MPNext, KMPNext, find_kmp


def test_MPNext():
    pattern = "ABACABAB"
    assert MPNext(pattern) == [-1, 0, 0, 1, 0, 1, 2, 3, 2]


def test_MPNext_pattern_zero_len():
    pattern = ""
    assert MPNext(pattern) == [-1]


def test_KMPNext():
    pattern = "ABACABAB"
    assert KMPNext(pattern) == [-1, 0, -1, 1, -1, 0, -1, 3, 2]


def test_KMPNext_pattern_zero_len():
    pattern = ""
    assert KMPNext(pattern) == [-1]


def test_KMP_simple():
    find_this = "Ala"
    text_to_be_searched = "Ala ma kota."
    assert find_kmp(find_this, text_to_be_searched) == [0]


def test_KMP_single_more_difficult():
    find_this = "Ala"
    text_to_be_searched = "Bla bla bla - Ala ma kota."
    # enumerating text:    0   4   8     14
    assert find_kmp(find_this, text_to_be_searched) == [14]


def test_KMP_numerous():
    find_this = "kot"
    text_to_be_searched = "kot KOT kot KOT kot pies"
    assert find_kmp(find_this, text_to_be_searched) == [0, 8, 16]


def test_KMP_numerous_nums_in_text():
    find_this = "5"
    text_to_be_searched = "3.14159265359"
    assert find_kmp(find_this, text_to_be_searched) == [5, 9, 11]


def test_KMP_no_pattern_occurring_in_text():
    find_this = "5"
    text_to_be_searched = "BALIN"
    assert find_kmp(find_this, text_to_be_searched) == []
