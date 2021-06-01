path = "graph1.txt"

def read_data(path):
    try:
        with open(path, 'r') as file_handle:
            data = []
            for line in file_handle:
                data_line = [int(char) for char in line[:-1]]
                data.append(data_line)
            return data
    except IsADirectoryError:
        print('File is a directory.')
    except FileNotFoundError:
        print('File not found.')


read_data(path)