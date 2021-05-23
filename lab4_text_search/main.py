from model_io import read_data, write_data
from words import get_words
from kmp import find_kmp
from naive import find_naive
from rabin_karp_pt import find_rk
from check_performance import check_performance


def run():
    data = read_data()
    words = get_words(data)
    result_kmp = check_performance(words, data, find_kmp)
    result_naive = check_performance(words, data, find_naive)
    result_rk = check_performance(words, data, find_rk)
    print(result_kmp, result_naive, result_rk)

    write_data([result_kmp, result_naive, result_rk])


run()
