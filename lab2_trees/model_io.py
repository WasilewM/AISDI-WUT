def read_data(file_handle):
    data = []
    for line in file_handle:
        data.append(line) if line[-1] != '\n' else data.append(line[:-1])
    return data


def write_data(file_handle, data):
    for line in data:
        file_handle.write(line + '\n')


def save_data(avl_results, bst_results):
    try:
        with open("create_trees_time_results.csv", 'w') as file_handle:
            results = []
            results.append(avl_results[0])
            results.append(bst_results[0])
            write_data(file_handle, results)
    except IsADirectoryError:
        print('Path is a directory.')

    try:
        with open("search_numbers_time_results.csv", 'w') as file_handle:
            results = []
            results.append(avl_results[1])
            results.append(bst_results[1])
            write_data(file_handle, results)
    except IsADirectoryError:
        print('Path is a directory.')

    try:
        with open("delete_numbers_time_results.csv", 'w') as file_handle:
            results = []
            results.append(avl_results[2])
            results.append(bst_results[2])
            write_data(file_handle, results)
    except IsADirectoryError:
        print('Path is a directory.')
