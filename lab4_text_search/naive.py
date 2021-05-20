def find_naive(pattern, text):
    """
    Finds pattern in given text. Uses naive pattern searching algorithm.
    Returns list conatining numbers that represent the char number in text
    from which the pattern occurring starts

    :param pattern: pattern to be found
    :type patter: str

    :param text: text to be checked for pattern occurring
    :type text: str
    """
    curr_text_fragment = ""
    first_char_idx = 0
    result = []

    while first_char_idx + len(pattern) < len(text):
        curr_text_fragment = text[first_char_idx:len(pattern) + first_char_idx]

        if curr_text_fragment == pattern:
            result.append(first_char_idx)

        first_char_idx += 1

    return result
