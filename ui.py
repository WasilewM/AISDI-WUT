import argparse
import sys

def main(arguments):
    """
    Main funcion of the console ui.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('FILENAME')
    args = parser.parse_args(arguments[1:])

    try:
        with open(args.FILENAME, 'r') as file_handle:
            pass
    except IsADirectoryError:
        print('File is a directory.')
    except FileNotFoundError:
        print('File not found.')

if __name__ == "__main__":
    main(sys.argv)
