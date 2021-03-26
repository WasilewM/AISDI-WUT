from bubble_sort import bubble_sort
from bucket_sort import bucket_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
import time


def check_bubble_sort_time(table_of_chars):
    results = ""
    signs_num = 500
    while signs_num < len(table_of_chars):
        t0 = time.time()
        bubble_sort(table_of_chars[:signs_num])
        signs_num += 500
        t1 = time.time()
        current_res = str(t1-t0)
        current_res = current_res[0] + ',' + current_res[2:]
        results += current_res + ';'
    return results


def check_bucket_sort_time(table_of_chars):
    results = ""
    signs_num = 500
    while signs_num < len(table_of_chars):
        t0 = time.time()
        bucket_sort(table_of_chars[:signs_num])
        signs_num += 500
        t1 = time.time()
        current_res = str(t1-t0)
        current_res = current_res[0] + ',' + current_res[2:]
        results += current_res + ';'
    return results


def check_merge_sort_time(table_of_chars):
    results = ""
    signs_num = 500
    while signs_num < len(table_of_chars):
        t0 = time.time()
        merge_sort(table_of_chars[:signs_num])
        signs_num += 500
        t1 = time.time()
        current_res = str(t1-t0)
        current_res = current_res[0] + ',' + current_res[2:]
        results += current_res + ';'
    return results


def check_quick_sort_time(table_of_chars):
    results = ""
    signs_num = 500
    while signs_num < len(table_of_chars):
        t0 = time.time()
        quick_sort(table_of_chars[:signs_num])
        signs_num += 500
        t1 = time.time()
        current_res = str(t1-t0)
        current_res = current_res[0] + ',' + current_res[2:]
        results += current_res + ';'
    return results
