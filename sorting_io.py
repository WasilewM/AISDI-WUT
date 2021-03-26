def read_data(file_handle):
    data = []
    for line in file_handle:
        data.append(line) if line[-1] != '\n' else data.append(line[:-1])
    return data


def write_data(file_handle, data):
    for line in data:
        file_handle.write(line + '\n')
