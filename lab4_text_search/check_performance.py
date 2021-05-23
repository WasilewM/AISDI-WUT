# from kmp import find_kmp
# from naive import find_naive
# from rabin_karp_pt import find_rk
import time
DELTA = 1e2
MAX_DELTA = 1e3


def check_performance(words, data, func):
    result = ""
    delta = DELTA

    while delta < MAX_DELTA:
        start_time = time.time()
        curr_word = 0

        while curr_word < delta:
            func(words[curr_word], data)
            curr_word += 1
        finish_time = time.time()

        result = result + str(finish_time - start_time) + ';'
        delta += DELTA

    return result
