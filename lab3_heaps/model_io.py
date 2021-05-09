def read_data(file_handle):
    data = []
    for line in file_handle:
        data.append(line) if line[-1] != '\n' else data.append(line[:-1])
    return data


def write_data(file_handle, data):
    for line in data:
        file_handle.write(line + '\n')


def save_data(bheap_results, theap_result, qheap_results):
    try:
        with open("create_heap_time_results.csv", 'w') as file_handle:
            results = []
            results.append(bheap_results[0])
            results.append(theap_result[0])
            results.append(qheap_results[0])
            write_data(file_handle, results)
    except IsADirectoryError:
        print('Path is a directory.')

    try:
        with open("pop_root_time_results.csv", 'w') as file_handle:
            results = []
            results.append(bheap_results[1])
            results.append(theap_result[1])
            results.append(qheap_results[1])
            write_data(file_handle, results)
    except IsADirectoryError:
        print('Path is a directory.')
