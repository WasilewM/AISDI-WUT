SOURCE_TEXT = "pan-tadeusz.txt"
OUTPUT_FILE = "results.csv"


def read_data():
    try:
        with open(SOURCE_TEXT, 'r') as file_handle:
            text = ""
            for line in file_handle:
                text = text + line
            return text
    except IsADirectoryError:
        print('File is a directory.')
    except FileNotFoundError:
        print('File not found.')


def write_data(data):
    with open(OUTPUT_FILE, 'w') as file_handle:
        for line in data:
            file_handle.write(line + '\n')
