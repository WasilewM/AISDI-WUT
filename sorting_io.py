def read_data(file_handle):
    data = []
    for line in file_handle:
        data.append(line) if line[-1] != '\n' else data.append(line[:-1])
    return data


def write_data(file_handle, data):
    for line in data:
        file_handle.write(line + '\n')


#     try:
#         with open(file, 'r') as file_handle:
#             read_data(file_handle)
#     except IsADirectoryError:
#         print('File is a directory.')
#     except FileNotFoundError:
#         print('File not found.')

#     try:
#         with open(file, 'r') as file_handle:
#             write_data(file_handle, data)
#     except IsADirectoryError:
#         print('Path is a directory.')
