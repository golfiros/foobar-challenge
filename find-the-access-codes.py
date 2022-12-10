def solution(l):
    n = len(l)
    # set up an adjacency list
    g = [[] for _ in range(n)]
    # fill it up by setting i -> j
    # whenever l[i] | l[j]
    for i in range(n):
        for j in range(i + 1, n):
            if l[j] % l[i] == 0:
                g[i].append(j)            

    # now just count how many neighbors
    # each neighbor has and add it all up
    count = 0
    for i in range(n):
        for j in g[i]:
            count += len(g[j])

    return count

print solution([1, 1, 1]) == 1
print solution([1, 2, 3, 4, 5, 6]) == 3
