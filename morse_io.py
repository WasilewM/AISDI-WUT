def read_data(path):
    data = []
    with open(path, 'r') as file_handle:
        for line in file_handle:
            data.append(line.capitalize()) if line[-1] != '\n' else data.append(line[:-1].capitalize())
    return data


def write_data(path, data):
    with open(path, 'w') as file_handle:
        file_handle.writelines(data)