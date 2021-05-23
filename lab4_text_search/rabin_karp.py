prime_num = 103
alphabet_len = 380
alphabet_offset = 32

def find_rk(pattern, text):
    result = []
    patt_len = len(pattern)
    text_len = len(text)

    patt_hash = 0
    text_hash = 0

    if not patt_len or not text_len:
        return None
    if patt_len > text_len:
        return None
    
    for char in pattern:
        hash_temp += (ord(char) - alphabet_offset) * alphabet_len ** (patt_len - pattern.index(char))
        