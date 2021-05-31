from model_io import read_data
import argparse
import sys


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('FILENAME')
    args = parser.parse_args(arguments[1:])

    data = read_data(args.FILENAME)
    print(data)


if __name__ == "__main__":
    main(sys.argv)
