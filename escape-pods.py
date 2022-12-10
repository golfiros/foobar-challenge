def solution(entrances, exits, paths):
    # this is a max-flow problem
    # we use a push-relabel algorithm available here:
    # https://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm
    
    # initial setup: 
    infinity = 100000000 # a large number

    # create proper source and sink nodes
    n = len(paths)
    capacity = [[0 for _ in range(n + 2)]] + [[0] + row + [0] for row in paths] + [[0 for _ in range(n + 2)]]
    for s in entrances:
        capacity[0][s + 1] = sum([paths[s][j] for j in range(n)])
    for t in exits:
        capacity[t + 1][-1] = sum([paths[j][t] for j in range(n)])

    # initialize what we'll be using in the algorithm
    n_nodes = n + 2
    queue = list(range(1, n_nodes - 1))

    flow = [[0] * n_nodes for _ in range(n_nodes)]
    excess = [0] * n_nodes
    def push(u, v):
        # pushes as much of the excess flow into u
        # through the edge (u,v)
        delta = min(excess[u], capacity[u][v] - flow[u][v])
        flow[u][v] += delta
        flow[v][u] -= delta
        excess[u] -= delta
        excess[v] += delta

    labels = [0] * n_nodes
    def relabel(u):
        # try to make a push possible by relabeling
        # u to be larger than some other v
        min_label = infinity
        for v in range(n_nodes):
            if capacity[u][v] > flow[u][v]:
                min_label = min(min_label, labels[v])
                labels[u] = min_label + 1

    seen = [0] * n_nodes
    def discharge(u):
        while excess[u] > 0:
            # try to see if we can move the excess into edges
            if seen[u] < n_nodes:
                v = seen[u]
                if capacity[u][v] > flow[u][v] and labels[u] > labels[v]:
                    push(u, v)
                else:
                    seen[u] += 1
            # if we can't then try a relabel
            else:
                relabel(u)
                seen[u] = 0

    labels[0] = n_nodes
    excess[0] = infinity
    for v in range(n_nodes):
        # push all of the excess into the entrance nodes
        push(0, v)

    p = 0 # node we're currently in
    while p < len(queue):
        u = queue[p]
        old_label = labels[u]
        discharge(u)
        if labels[u] > old_label:
            # if the label increased we move it
            # to the top of the list and restart
            queue.insert(0, queue.pop(p))
            p = 0
        else:
            p += 1

    # sum everything coming from the source and output that
    return sum(flow[0])

print solution([0],[3],[[0,7,0,0],
                        [0,0,6,0],
                        [0,0,0,8],
                        [9,0,0,0]
                        ]) == 6

print solution([0],[3],[[0,1000,1000,0],
                        [0,0,1,1000],
                        [0,0,0,1000],
                        [0,0,0,0]
                        ]) == 2000

print solution([0,1],[4, 5],[[0,0,4,6,0,0],
                             [0,0,5,2,0,0],
                             [0,0,0,0,4,4],
                             [0,0,0,0,6,6],
                             [0,0,0,0,0,0],
                             [0,0,0,0,0,0]
                             ]) == 16

print solution([0],[5],[[0,11,12,0,0,0],
                        [0,0,0,12,0,0],
                        [0,1,0,0,11,0],
                        [0,0,0,0,0,19],
                        [0,0,0,7,0,4],
                        [0,0,0,0,0,0]
                        ]) == 23

print solution([0],[5],[[0,10,10,0,0,0],
                        [0,0,2,4,8,0],
                        [0,0,0,0,9,0],
                        [0,0,0,0,0,10],
                        [0,0,0,6,0,10],
                        [0,0,0,0,0,0]
                        ]) == 19

print solution([0],[6],[[0,3,0,3,0,0,0],
                        [0,0,4,0,0,0,0],
                        [3,0,0,1,2,0,0],
                        [0,0,0,0,2,6,0],
                        [0,1,0,0,0,0,1],
                        [0,0,0,0,0,0,9],
                        [0,0,0,0,0,0,0],
                        ]) == 5
