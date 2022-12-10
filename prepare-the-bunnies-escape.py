def dijkstra(graph):
    # simple dijkstra's algorithm
    # finds length of shortest path between
    # between first and last vertex of graph
    n = len(graph)
    infinity = 100000000
    dist = [0] + [infinity] * (n - 1)
    prev = [-1] * n
    queue = list(range(n))
    
    while queue:
        min_dist = infinity + 1
        u = -1
        for v in queue:
            if dist[v] < min_dist:
                min_dist = dist[v]
                u = v
        if u == n - 1:
            break
        queue.remove(u)
        for v in [x for x in graph[u] if x in queue]:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist[-1]
    
def solution(map):
    w = len(map)
    h = len(map[0])
    n = h * w
    
    # we're going to construct a directed
    # graph representing the maze

    # we need some helper functions to
    # translate between vertex indices and
    # the corresponding coordinates
    def index(x, y):
        return h * x + y

    def coordinate(u):
        x = u / h
        y = u % h
        return x, y

    # get the cardinal directions going
    def neighbors(u):
        x, y = coordinate(u)
        if x > 0:
            yield index(x - 1, y)
        if x < w - 1:
            yield index(x + 1, y)
        if y > 0:
            yield index(x, y - 1)
        if y < h - 1:
            yield index(x, y + 1)

    # and represent the entire map as a single list
    map_flat = []
    for row in map:
        map_flat += row

    # to be able to break a single wall we'll have
    # two copies of the maze encoded in the graph
    graph = [[] for _ in range(2 * n)]
    for u in range(n):
        for v in neighbors(u):
            if map_flat[u] == 0:
                # in the first copy we can move in any 
                # direction if we start from a free vertex
                graph[u].append(v)
            if map_flat[v] == 0:
                # and in the second we can move from
                # any direction into a free vertex
                graph[n + u].append(n + v)
        # and at any time we can jump from the first
        # graph to the second, but not the other way
        # around
        graph[u].append(n + u)
    
    # breaking a single wall is then translated as
    # walking into a wall, hopping to the copy,
    # and then walking out of the wall

    # by construction this happens at most once
    # if we wanted to allow multiple breakages
    # we'd just add more and more copies of
    # the original maze

    # to finish we just find the shortest path
    return dijkstra(graph)

print solution([[0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 1, 1, 0]
                ]) == 7

print solution([[0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]
                ]) == 11
