from dijkstra import dijkstra, BIG_NUM
from model_io import read_data
import argparse
import sys


def reorganise_data(data):
    new_data = []
    boarder = []
    new_row_item_count = len(data[0])
    added_items = 0

    while added_items < new_row_item_count + 2:
        boarder.append(BIG_NUM)
        added_items += 1

    new_data.append(boarder)

    for row in data:
        new_row = []
        new_row.append(BIG_NUM)

        for number in row:
            new_row.append(number)

        new_row.append(BIG_NUM)
        new_data.append(new_row)

    new_data.append(boarder)
    return new_data

def find_zeros(data):
    zeros = []
    for line in data:
        for value in line:
            if value == 0:
                x = line.index(value)
                y = data.index(line)
                zeros.append((x, y))
            if len(zeros) == 2:
                return zeros


def init_distance_table(data):
    distance_table = []

    for _ in data:
        dist_row = []
        for _ in data:
            dist_row.append(BIG_NUM)
        distance_table.append(dist_row)

    return distance_table


def print_table(table):
    for data_row in table:
        print(data_row)


def main(arguments):
    # parser = argparse.ArgumentParser()
    # parser.add_argument('FILENAME')
    # args = parser.parse_args(arguments[1:])
    # data = read_data(args.FILENAME)
    data = read_data("graph1.txt")
    data = reorganise_data(data)
    zeros = find_zeros(data)
    distance_table = init_distance_table(data)
    dijkstra(data, distance_table, zeros[0], zeros[1])

    print_table(distance_table)
    print('\n')
    print_table(data)
    # print(zeros)
    # print(distance_table)


# if __name__ == "__main__":
#     main(sys.argv)

main(1)