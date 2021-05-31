from model_io import read_data
import argparse
import sys


def find_zero(data):
    for line in data:
        for char in line:
            if char == '0':
                x = line.index(char)
                y = data.index(line)
                return (x, y)


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('FILENAME')
    args = parser.parse_args(arguments[1:])

    data = read_data(args.FILENAME)
    print(data)
    print(find_zero(data))


if __name__ == "__main__":
    main(sys.argv)
