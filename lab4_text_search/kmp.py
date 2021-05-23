def MPNext(pattern):
    """
    Finds maximum prefixo-sufixes in given pattern.
    Returns PI_table as a result. PI_table contains length of the
    maximum prefixo-sufixes in reference to the length of the
    pattern substring

    :param pattern: pattern to be checked for prefixo-sufixes
    :type patter: str
    """
    PI_table = []
    PI_table.append(-1)

    if len(pattern) < 1:
        return PI_table

    pattern = "0" + pattern
    idx = 1
    curr_pref_length = -1
    while idx < len(pattern):
        while (
            curr_pref_length >= 0 and
            pattern[curr_pref_length+1] != pattern[idx]
        ):
            curr_pref_length = PI_table[curr_pref_length]

        curr_pref_length += 1
        PI_table.append(curr_pref_length)
        idx += 1

    return PI_table


def KMPNext(pattern):
    """
    Finds maximum prefixo-sufixes in given pattern.
    Returns PI_table as a result. PI_table contains length of the
    maximum prefixo-sufixes in reference to the length of the
    pattern substring and the first char after the prefix

    :param pattern: pattern to be checked for prefixo-sufixes
    :type patter: str
    """
    PI_table = []
    PI_table.append(-1)

    if len(pattern) < 1:
        return PI_table

    # pattern = "0" + pattern
    idx = 1
    curr_pref_length = -1
    while idx <= len(pattern):
        while (
            curr_pref_length >= 0 and
            pattern[curr_pref_length] != pattern[idx - 1]
        ):
            curr_pref_length = PI_table[curr_pref_length]

        curr_pref_length += 1

        if idx == len(pattern) or pattern[idx] != pattern[curr_pref_length]:
            PI_table.append(curr_pref_length)
        else:
            PI_table.append(PI_table[curr_pref_length])

        idx += 1

    return PI_table


def find_kmp(pattern, text):
    """
    Finds pattern in given text. Uses kmp algorithm for pattern searching.
    Returns list conatining numbers that represent the char number in text
    from which the pattern occurring starts

    :param pattern: pattern to be found
    :type patter: str

    :param text: text to be checked for pattern occurring
    :type text: str
    """
    curr_pref_len = 0
    idx = 0
    result = []

    if not len(pattern) or not len(text):
        return []
    if len(pattern) > len(text):
        return []

    PI_table = KMPNext(pattern)

    while idx < len(text):
        while (
            curr_pref_len > -1 and
            pattern[curr_pref_len] != text[idx]
        ):
            curr_pref_len = PI_table[curr_pref_len]

        curr_pref_len += 1
        if curr_pref_len == len(pattern):
            result.append(idx - curr_pref_len + 1)
            curr_pref_len = PI_table[curr_pref_len]

        idx += 1

    return result
