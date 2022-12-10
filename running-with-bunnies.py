def bellman_ford(weights): # find min times to reach exit
    inf = 1000000000 # large number
    n = len(weights) # existence of negative cycles
    dist = [inf] * (n - 1) + [0]
    for _ in range(n - 1): # find shortest paths
        for i in range(n):
            for j in [x for x in range(n) if x != i]:
                if dist[i] + weights[j][i] < dist[j]:
                    dist[j] = dist[i] + weights[j][i]
    for i in range(n):
        for j in [x for x in range(n) if x != i]:
            if dist[i] + weights[j][i] < dist[j]:
                return(True, None) # there exists a negative cycle
    return (False, dist)
    
def detect_circle(path): # detect cycles in path
    seq = list(reversed(path))
    for i in range(2, len(seq) / 2):
        if seq[0:i] == seq[i:2 * i]:
            return True
    return False
    
def get_bunnies(path, n): # find bunnies gathered
    bun_list = []
    for b in range(0, n - 2):
        if b + 1 in path:
            bun_list.append(b)
    return bun_list
    
def compare_bunnies(x, y): # comparing lists of bunnies
    n = len(x)
    if n > len(y):
        return True
    if n < len(y):
        return False
    for i in range(n):
        if x[i] < y[i]:
            return True
    return False
    
def solution(times, times_limit):
    n = len(times)
    neg_flag, exit_times = bellman_ford(times)
    if neg_flag: # if we have a negative cycle we can save everyone
        return list(range(n - 2))
    # try out all reasonable paths in dfs
    bunnies = []
    path_stack = [([0],times_limit)]
    while path_stack:
        curr_path, curr_time = path_stack.pop()
        curr_node = curr_path[-1]
        if detect_circle(curr_path) or len(curr_path) > 2 * (n - 1): 
            # skip if circling or meandering
            # why does 2 * (n - 1) work?
            continue
        if curr_node == n - 1:
            # if we're at the end this is a valid path
            bun = get_bunnies(curr_path, n)
            if len(bun) == n - 2:
                # stop early if we managed to get all bunnies
                bunnies = bun
                break
            if compare_bunnies(bun, bunnies):
                bunnies = bun
        for v in [x for x in range(n) if x != curr_node and exit_times[x] + times[curr_node][x] <= curr_time]:
            # generate next viable paths
            path_stack.append((curr_path + [v], curr_time - times[curr_node][v]))
    # sort entries and return first
    return bunnies

print solution([[0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0]
                ], 3) == [0, 1]

print solution([[0, 2, 2, 2, -1],
                [9, 0, 2, 2, -1],
                [9, 3, 0, 2, -1],
                [9, 3, 2, 0, -1],
                [9, 3, 2, 2, 0]
                ], 1) == [1, 2]
