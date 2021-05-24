ab_map = {
    " ": 0,     "A": 45,    "!": 90,
    "-": 1,     "Ą": 46,    '"': 91,
    ";": 2,     "B": 47,    "/": 92,
    ",": 3,     "C": 48,    "\n": 93,
    ".": 4,     "Ć": 49,    "—": 94,
    ":": 5,     "D": 50,    "é": 95,
    "(": 6,     "E": 51,    "…": 96,
    ")": 7,     "Ę": 52,    "«": 97,
    "?": 8,     "F": 53,    "»": 98,
    "*": 9,     "G": 54,    "à": 99,
    "a": 10,    "H": 55,    "æ": 100,
    "ą": 11,    "I": 56,    "–": 101,
    "b": 12,    "J": 57,
    "c": 13,    "K": 58,
    "ć": 14,    "L": 59,
    "d": 15,    "Ł": 60,
    "e": 16,    "M": 61,
    "ę": 17,    "N": 62,
    "f": 18,    "Ń": 63,
    "g": 19,    "O": 64,
    "h": 20,    "Ó": 65,
    "i": 21,    "P": 66,
    "j": 22,    "Q": 67,
    "k": 23,    "R": 68,
    "l": 24,    "S": 69,
    "ł": 25,    "Ś": 70,
    "m": 26,    "T": 71,
    "n": 27,    "U": 72,
    "ń": 28,    "V": 73,
    "o": 29,    "W": 74,
    "ó": 30,    "X": 75,
    "p": 31,    "Y": 76,
    "q": 32,    "Z": 77,
    "r": 33,    "Ź": 78,
    "s": 34,    "Ż": 79,
    "ś": 35,    "0": 80,
    "t": 36,    "1": 81,
    "u": 37,    "2": 82,
    "v": 38,    "3": 83,
    "w": 39,    "4": 84,
    "x": 40,    "5": 85,
    "y": 41,    "6": 86,
    "z": 42,    "7": 87,
    "ź": 43,    "8": 88,
    "ż": 44,    "9": 89
}

prime_num = 1610612741

alphabet_len = len(ab_map.keys())

def find_rk_map(pattern, text):
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
        patt_hash += ab_map[pattern[i]] * (alphabet_len ** (patt_len - i - 1))
        text_hash += ab_map[text[i]] * (alphabet_len ** (patt_len - i - 1))

    patt_hash = patt_hash % prime_num
    text_hash = text_hash % prime_num

    while first_char_idx + patt_len <= text_len:
        if patt_hash == text_hash:
            text_fragment = text[first_char_idx:len(pattern) + first_char_idx]
            if text_fragment == pattern:
                result.append(first_char_idx)

        first_char_idx += 1
        if first_char_idx <= text_len - patt_len:
            new_hash = (text_hash - ((alphabet_len ** (patt_len - 1)) % prime_num) * ab_map[text[first_char_idx - 1]]) % prime_num
            new_hash = (new_hash * alphabet_len) % prime_num
            new_hash = (new_hash + ab_map[text[first_char_idx + patt_len - 1]]) % prime_num
            text_hash = new_hash

    return result
