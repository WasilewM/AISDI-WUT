import queue
BIG_NUM = 100


def dijkstra(data, distance_table, start, end):
    # setup
    y0, x0 = start
    distance_table[y0][x0] = 0
    visited_nodes = set()
    # mark end node
    visited_nodes.add(end)

    # initializing queue for Dijktra algorothm
    dijktra_queue = queue.Queue()
    dijktra_queue.put((y0, x0))

    while not dijktra_queue.empty():
        y_curr, x_curr = dijktra_queue.get()

        if (y_curr, x_curr) not in visited_nodes:
            # adding nodes items to dijkstra_queue
            # try - except blocks to prevent Errors
            # (index out of range)
            try:
                if data[y_curr-1][x_curr] != BIG_NUM:
                    dijktra_queue.put((y_curr - 1, x_curr))
            except IndexError:
                pass
            try:
                if data[y_curr][x_curr-1] != BIG_NUM:
                    dijktra_queue.put((y_curr, x_curr - 1))
            except IndexError:
                pass
            try:
                if data[y_curr+1][x_curr] != BIG_NUM:
                    dijktra_queue.put((y_curr + 1, x_curr))
            except IndexError:
                pass
            try:
                if data[y_curr][x_curr+1] != BIG_NUM:
                    dijktra_queue.put((y_curr, x_curr + 1))
            except IndexError:
                pass

            #  updating distance values
            try:
                if data[y_curr-1][x_curr] + distance_table[y_curr][x_curr] < distance_table[y_curr-1][x_curr]:
                    distance_table[y_curr-1][x_curr] = data[y_curr-1][x_curr] + distance_table[y_curr][x_curr]
            except IndexError:
                pass
            try:
                if data[y_curr][x_curr-1] + distance_table[y_curr][x_curr] < distance_table[y_curr][x_curr-1]:
                    distance_table[y_curr][x_curr-1] = data[y_curr][x_curr-1] + distance_table[y_curr][x_curr]
            except IndexError:
                pass
            try:
                if data[y_curr+1][x_curr] + distance_table[y_curr][x_curr] < distance_table[y_curr+1][x_curr]:
                    distance_table[y_curr+1][x_curr] = data[y_curr+1][x_curr] + distance_table[y_curr][x_curr]
            except IndexError:
                pass
            try:
                if data[y_curr][x_curr+1] + distance_table[y_curr][x_curr] < distance_table[y_curr][x_curr+1]:
                    distance_table[y_curr][x_curr+1] = data[y_curr][x_curr+1] + distance_table[y_curr][x_curr]
            except IndexError:
                pass
        # marking the node as visited
        visited_nodes.add((y_curr, x_curr))

    return distance_table
