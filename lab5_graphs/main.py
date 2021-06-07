from dijkstra import dijkstra, BIG_NUM
from model_io import read_data
import argparse
import sys


shortest_path = []

def reorganise_data(data):
    """
    Preprocesses data for the use of Dijkstra algorithm.
    """
    # init tables
    new_data = []
    boarder = []
    new_row_item_count = len(data[0])
    added_items = 0
    # created a row of BIG_NUM
    # this will be used as a boarder in order not to
    # create a IndexError ind Dijkstra algorithm
    while added_items < new_row_item_count + 2:
        boarder.append(BIG_NUM)
        added_items += 1

    new_data.append(boarder)

    for row in data:
        new_row = []
        # adding BIG_NUM to the first column of the row
        # this will be used as a boarder in order not to
        # create a IndexError ind Dijkstra algorithm
        new_row.append(BIG_NUM)

        # appending numbers from the data
        for number in row:
            new_row.append(number)

        # adding BIG_NUM to the last column of the row
        # this will be used as a boarder in order not to
        # create a IndexError ind Dijkstra algorithm
        new_row.append(BIG_NUM)
        new_data.append(new_row)

    # appending the last row - consisting of BIG_NUM
    # this will be used as a boarder in order not to
    # create a IndexError ind Dijkstra algorithm
    new_data.append(boarder)
    return new_data


def find_zeros(data):
    """
    Finds and returns table of coordinates of zeros
    from data.
    """
    # init table
    zeros = []
    cols_num = len(data)
    rows_num = len(data[0])
    # look for zeros
    for y in range(cols_num - 1):
        for x in range(rows_num - 1):
            # if zero found, append its
            # coordinates to the zeros table
            if data[y][x] == 0:
                zeros.append((y, x))
    # return the result
    return zeros


def init_distance_table(data):
    """
    Initializes distance table for the use of
    Dijkstra algorithm.
    """
    distance_table = []

    # append rows consisting of BIG_NUM values
    for _ in data:
        dist_row = []
        for _ in data:
            dist_row.append(BIG_NUM)
        distance_table.append(dist_row)

    # return the result
    return distance_table


def print_table(table):
    """
    Prints the table in a more readable way.
    """
    for data_row in table:
        print(data_row)


def get_shortest_path(distance_table, start, end):
    if end != start:
        y, x = end

        smallest = min(
            distance_table[y][x+1],
            distance_table[y+1][x],
            distance_table[y-1][x],
            distance_table[y][x-1]
        )
        if smallest == distance_table[y][x+1]:
            end = y, x + 1
            shortest_path.append(end)
        elif smallest == distance_table[y+1][x]:
            end = y + 1, x
            shortest_path.append(end)
        elif smallest == distance_table[y-1][x]:
            end = y - 1, x
            shortest_path.append(end)
        elif smallest == distance_table[y][x-1]:
            end = y, x - 1
            shortest_path.append(end)

        get_shortest_path(distance_table, start, end)

    return shortest_path


def main(arguments):
    """
    Main function.
    Parses given arguments and if the data are correct, calls for
    the Dijkstra algorithm.
    """
    # parse the arguments
    # parser = argparse.ArgumentParser()
    # parser.add_argument('FILENAME')
    # args = parser.parse_args(arguments[1:])
    # read data
    data = read_data("graph1.txt")

    # preprocess the data for the Dijkstra algorithm
    data = reorganise_data(data)
    zeros = find_zeros(data)

    # checking the number of zeros
    # if there are exactly 2, then proceeds the Dijkstra algorithm
    if len(zeros) != 2:
        print("Invalid input data. Check the file\n")
    else:
        distance_table = init_distance_table(data)
        # call dijkstra algorithm
        distance_table = dijkstra(data, distance_table, zeros[0])
        # print results
        print_table(distance_table)

        shortest_path = get_shortest_path(distance_table, zeros[0], zeros[1])
        print(shortest_path)

main(1)
# if __name__ == "__main__":
#     main(sys.argv)
