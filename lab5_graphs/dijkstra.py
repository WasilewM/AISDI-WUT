import queue
BIG_NUM = 100


def add_neighbours_to_queue(y, x, data, dijkstra_queue):
    """
    Suplementary function for dijkstra().
    Updates the dijkstra_queue used in Dijkstra algorithm.
    """
    if data[y-1][x] != BIG_NUM:
        dijkstra_queue.put((data[y-1][x], y - 1, x))

    if data[y][x-1] != BIG_NUM:
        dijkstra_queue.put((data[y][x-1], y, x - 1))

    if data[y+1][x] != BIG_NUM:
        dijkstra_queue.put((data[y+1][x], y + 1, x))

    if data[y][x+1] != BIG_NUM:
        dijkstra_queue.put((data[y][x+1], y, x + 1))

    return dijkstra_queue


def dijkstra(data, dist, start):
    """
    Dijkstra algorithm. Calculates the shortests distances
    between given start node and the rest od the nodes
    """
    # setup
    y0, x0 = start
    dist[y0][x0] = 0
    visited_nodes = set()

    # initializing queue for Dijktra algorothm
    dijkstra_queue = queue.PriorityQueue()
    dijkstra_queue.put((0, y0, x0))

    while not dijkstra_queue.empty():
        # y, x - coordinates of the "node"
        # curr_node_data used only to prioritise nodes in dijkstra_queue
        curr_node_data, y, x = dijkstra_queue.get()

        if (y, x) not in visited_nodes:
            # adding nodes items to dijkstra_queue
            dijkstra_queue = add_neighbours_to_queue(
                y, x, data, dijkstra_queue
            )

            #  updating distance values
            if data[y-1][x] + dist[y][x] < dist[y-1][x]:
                dist[y-1][x] = data[y-1][x] + dist[y][x]
                # if modified node has already been visited,
                # it should be removed from the visited_nodes set
                # in order to assure that the update of its neghbours
                # can be done
                if (y - 1, x) in visited_nodes:
                    visited_nodes.remove((y - 1, x))
                # call for add_neighbours_to_queue to update the
                # dijkstra_queue
                dijkstra_queue = add_neighbours_to_queue(
                    y - 1, x, data, dijkstra_queue
                )

            if data[y][x-1] + dist[y][x] < dist[y][x-1]:
                dist[y][x-1] = data[y][x-1] + dist[y][x]
                # if modified node has already been visited,
                # it should be removed from the visited_nodes set
                # in order to assure that the update of its neghbours
                # can be done
                if (y, x - 1) in visited_nodes:
                    visited_nodes.remove((y, x - 1))
                # call for add_neighbours_to_queue to update the
                # dijkstra_queue
                dijkstra_queue = add_neighbours_to_queue(
                    y, x - 1, data, dijkstra_queue
                )

            if data[y+1][x] + dist[y][x] < dist[y+1][x]:
                dist[y+1][x] = data[y+1][x] + dist[y][x]
                # if modified node has already been visited,
                # it should be removed from the visited_nodes set
                # in order to assure that the update of its neghbours
                # can be done
                if (y + 1, x) in visited_nodes:
                    visited_nodes.remove((y + 1, x))
                # call for add_neighbours_to_queue to update the
                # dijkstra_queue
                dijkstra_queue = add_neighbours_to_queue(
                    y + 1, x, data, dijkstra_queue
                )

            if data[y][x+1] + dist[y][x] < dist[y][x+1]:
                dist[y][x+1] = data[y][x+1] + dist[y][x]
                # if modified node has already been visited,
                # it should be removed from the visited_nodes set
                # in order to assure that the update of its neghbours
                # can be done
                if (y, x + 1) in visited_nodes:
                    visited_nodes.remove((y, x + 1))
                # call for add_neighbours_to_queue to update the
                # dijkstra_queue
                dijkstra_queue = add_neighbours_to_queue(
                    y, x + 1, data, dijkstra_queue
                )

        # marking the node as visited
        visited_nodes.add((y, x))

    return dist
