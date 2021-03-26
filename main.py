from sorting_io import read_data, write_data
from measure_times import (
    check_bubble_sort_time,
    check_bucket_sort_time,
    check_merge_sort_time,
    check_quick_sort_time
)


def init_data():
    try:
        with open("lorem_ipsum.txt", 'r') as file_handle:
            data = read_data(file_handle)
    except IsADirectoryError:
        print('File is a directory.')
    except FileNotFoundError:
        print('File not found.')

    return data


def init_table(data):
    table_of_chars = []
    for line in data:
        for char in line:
            table_of_chars.append(char)
    return table_of_chars


def save_data(data):
    try:
        with open("sorting_algorithms_time_results.csv", 'w') as file_handle:
            write_data(file_handle, data)
    except IsADirectoryError:
        print('Path is a directory.')

    try:
        with open("sorting_algorithms_time_results.txt", 'w') as file_handle:
            write_data(file_handle, data)
    except IsADirectoryError:
        print('Path is a directory.')


def main():
    results = []
    input_data = init_data()
    table_of_chars = init_table(input_data)
    res = check_bubble_sort_time(table_of_chars)
    results.append(res)

    table_of_chars = init_table(input_data)
    res = check_bucket_sort_time(table_of_chars)
    results.append(res)

    table_of_chars = init_table(input_data)
    res = check_merge_sort_time(table_of_chars)
    results.append(res)

    table_of_chars = init_table(input_data)
    res = check_quick_sort_time(table_of_chars)
    results.append(res)

    save_data(results)


main()
