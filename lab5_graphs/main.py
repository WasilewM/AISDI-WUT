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
        shortest_path.append(end)

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


def create_path_image(path, path_image, data):
    """
    Transforst list path_image to represent the path in the form
    of "image".
    """
    # marking nodes that creathe the shortest path
    for y, x in path:
        path_image[y][x] = data[y][x]

    # mark nodes that do not belong to the shortest path as ' '
    #
    y = 1
    x = 1
    while y < len(path_image) - 1:
        while x < len(path_image[y]) - 1:
            if path_image[y][x] == BIG_NUM:
                path_image[y][x] = ' '
            x += 1

        y += 1
        x = 1

    # creating the image - the result
    image = ""
    for row in path_image:
        nodes_amount = 0
        for node in row:
            # appending nodes to image
            if node != BIG_NUM:
                image = image + str(node)
                nodes_amount += 1
        # appending new line
        if nodes_amount != 0:
            image += '\n'

    return image


def main(arguments):
    """
    Main function.
    Parses given arguments and if the data are correct, calls for
    the Dijkstra algorithm.
    """
    # parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('FILENAME')
    args = parser.parse_args(arguments[1:])
    # read data
    data = read_data(args.FILENAME)

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
        # print results just to check them
        # print_table(distance_table)

        shortest_path = get_shortest_path(distance_table, zeros[0], zeros[1])
        # printing results just to check them
        # print(shortest_path)

        # using init_distance_table to get correct size for path image list
        # containing lists
        path_image = init_distance_table(data)
        path_image = create_path_image(shortest_path, path_image, data)
        print(path_image)


if __name__ == "__main__":
    main(sys.argv)
