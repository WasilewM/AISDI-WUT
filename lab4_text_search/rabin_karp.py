# prime_num = 103
# last_char_num = 380
# alphabet_offset = 32

prime_num = 23
last_char_num = ord("B")
alphabet_offset = ord("A")

alphabet_len = last_char_num - alphabet_offset + 1


def find_rk(pattern, text):
    """
    Finds pattern in given text. Uses Rabin-Karp algorithm for pattern
    searching.
    Returns list conatining numbers that represent the char number in text
    from which the pattern occurring starts

    :param pattern: pattern to be found
    :type patter: str

    :param text: text to be checked for pattern occurring
    :type text: str
    """
    result = []
    patt_len = len(pattern)
    text_len = len(text)
    first_char_idx = 0

    patt_hash = 0
    text_hash = 0

    if not patt_len or not text_len:
        return []
    if patt_len > text_len:
        return []

    for i in range(patt_len):
        patt_hash += (ord(pattern[i]) - alphabet_offset) * (alphabet_len ** (patt_len - i - 1))
        text_hash += (ord(text[i]) - alphabet_offset) * (alphabet_len ** (patt_len - i - 1))

    patt_hash = patt_hash % prime_num
    text_hash = text_hash % prime_num

    while first_char_idx + patt_len <= text_len:
        if patt_hash == text_hash:
            text_fragment = text[first_char_idx:len(pattern) + first_char_idx]
            if text_fragment == pattern:
                result.append(first_char_idx)

        first_char_idx += 1
        if first_char_idx <= text_len - patt_len:
            new_hash = (text_hash - ((alphabet_len ** (patt_len - 1)) % prime_num) * (ord(text[first_char_idx - 1]) - alphabet_offset)) % prime_num
            new_hash = (new_hash * alphabet_len) % prime_num
            new_hash = (new_hash + ord(text[first_char_idx + patt_len - 1]) - alphabet_offset) % prime_num
            text_hash = new_hash

    return result
