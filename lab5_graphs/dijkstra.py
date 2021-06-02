import queue
BIG_NUM = 100


def dijkstra(data, dist, start, end):
    # setup
    y0, x0 = start
    dist[y0][x0] = 0
    visited_nodes = set()
    # mark end node
    y_end, x_end = end
    visited_nodes.add((y_end, x_end))

    # initializing queue for Dijktra algorothm
    dijktra_queue = queue.PriorityQueue()
    dijktra_queue.put((0, y0, x0))

    while not dijktra_queue.empty():
        # y, x - coordinates of the "node"
        dist_curr, y, x = dijktra_queue.get()

        if (y, x) not in visited_nodes:
            # adding nodes items to dijkstra_queue
            # try - except blocks to prevent Errors
            # (index out of range)
            if data[y-1][x] != BIG_NUM:
                dijktra_queue.put((data[y-1][x], y - 1, x))

            if data[y][x-1] != BIG_NUM:
                dijktra_queue.put((data[y][x-1], y, x - 1))

            if data[y+1][x] != BIG_NUM:
                dijktra_queue.put((data[y+1][x], y + 1, x))

            if data[y][x+1] != BIG_NUM:
                dijktra_queue.put((data[y][x+1], y, x + 1))

            #  updating distance values
            if data[y-1][x] + dist[y][x] < dist[y-1][x]:
                dist[y-1][x] = data[y-1][x] + dist[y][x]

            if data[y][x-1] + dist[y][x] < dist[y][x-1]:
                dist[y][x-1] = data[y][x-1] + dist[y][x]

            if data[y+1][x] + dist[y][x] < dist[y+1][x]:
                dist[y+1][x] = data[y+1][x] + dist[y][x]

            if data[y][x+1] + dist[y][x] < dist[y][x+1]:
                dist[y][x+1] = data[y][x+1] + dist[y][x]

        # marking the node as visited
        visited_nodes.add((y, x))

    return dist
