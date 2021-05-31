def read_data(path):
    try:
        with open(path, 'r') as file_handle:
            data = []
            for line in file_handle:
                data_line = [char for char in line]
                data.append(data_line)
            return data_line
    except IsADirectoryError:
        print('File is a directory.')
    except FileNotFoundError:
        print('File not found.')
