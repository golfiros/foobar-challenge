from fractions import gcd

def loops(a, b):
    # check if two trainers go in a loop or not
    # if they equalized they're bored
    if a == b:
        return False
    # but if they have an odd number of bananas 
    # in total, they're never going to equalize
    if (a + b) % 2 == 1:
        return True
    # do an iteration of the game
    a, b = min(a, b), max(a, b)
    b = b - a
    a = 2 * a
    # and divide through by the gcd to make the
    # numbers without affecting the result
    d = gcd(a, b)
    a /= d
    b /= d
    return loops(a, b)
    
from collections import deque

class blossom:
    # algorithm taken from Tarjan's
    # Data Structures and Network Algorithms
    def __init__(self, n):
        # initialize everything so we don't do
        # a bunch of allocations during runtime
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.pointer = [-1] * n
        self.rank = [-1] * n
        self.node_colors = [0] * n
        self.origin = list(range(self.n))
        self.pred = [-1] * n
        self.bridge = [(-1,-1)] * n
        self.matching = [-1] * n

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    # helper methods for disjoint set manipulation
    def makeset(self, x):
        self.pointer[x] = x
        self.rank[x] = 0
    
    def find(self, x):
        if x != self.pointer[x]:
            self.pointer[x] = self.find(self.pointer[x])
        return self.pointer[x]
    
    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.pointer[y] = x
            return x
        elif self.rank[x] == self.rank[y]:
            self.rank[y] = self.rank[y] + 1
        self.pointer[x] = y
        return y
    
    # get parent in alternating tree
    def parent(self, x):
        if self.node_colors[x] == 1:
            return self.matching[x]
        elif self.node_colors[x] == -1:
            return self.pred[self.origin[self.find(x)]]
        else:
            return -1
    
    # construct an alternating path between two vertices
    # with built in blossom expansion
    def path(self, v, w):
        if v == w:
            return [v]
        if self.node_colors[v] == 1:
            return [v, self.matching[v]] + self.path(self.pred[self.matching[v]], w)
        elif self.node_colors[v] == -1:
            return [v] + list(reversed(self.path(self.bridge[v][0], self.matching[v]) + self.path(self.bridge[v][1], w)))
        return []

    # find an augmenting path in the current graph
    def find_augmenting_path(self):
        # reset any blossom contractions
        self.origin = list(range(self.n))
        for u in self.origin:
            self.makeset(u)

        # create a queue for edges to explore
        relevant_edges = deque((v, w) for v in range(self.n) if self.matching[v] == -1 for w in self.graph[v])
        # and reset node colors: 1 is even, -1 is odd, and 0 is unreached
        self.node_colors = [1 if self.matching[v] == -1 else 0 for v in range(self.n)]
    
        # start constructing the forest
        aug_path = []
        while relevant_edges:
            (v, w) = relevant_edges.popleft()
            # get the effective contracted verts
            v_new = self.origin[self.find(v)]
            w_new = self.origin[self.find(w)]
            if self.node_colors[w_new] == 0:
                # if a vert is unreached we add it to the
                # current tree, as well as its mate
                self.node_colors[w_new] = -1
                x = self.matching[w_new]
                self.node_colors[x] = 1
                # add the mate's neighbors to our queue
                for y in self.graph[x]:
                    relevant_edges.append((x, y))
                self.pred[w_new] = v
            elif self.node_colors[w_new] == 1:
                # otherwise if a vert is even
                # one of two interesting things happened
                # find the paths to the respective roots
                path_v = [v_new] + [-1] * self.n
                path_w = [w_new] + [-1] * self.n
                root_v = 0
                root_w = 0
                for i in range(self.n + 1):
                    if path_v[i] == -1:
                        root_v = i
                        break
                    path_v[i + 1] = self.parent(path_v[i])
                for i in range(self.n + 1):
                    if path_w[i] == -1:
                        root_w = i
                        break
                    path_w[i + 1] = self.parent(path_w[i])
                if path_v[root_v - 1] != path_w[root_w - 1]:
                    # if the verts belong to different trees
                    # we have found an alternating path between
                    # exposed verts, an augmenting path
                    aug_path = list(reversed(self.path(v, path_v[root_v - 1]))) + self.path(w, path_w[root_w - 1])
                    break
                elif v_new != w_new:
                    # otherwise we found a blossom and need
                    # to contract it

                    # find the base
                    while root_v > 0 and root_w > 0 and path_v[root_v - 1] == path_w[root_w - 1]:
                        root_v -= 1
                        root_w -= 1
                    u = path_v[root_v]
                    # add all of the blossom's verts to the
                    # base's set and mark all odd verts' 
                    # edges to be explored, as they have now
                    # been contracted and are effectively even
                    for x in path_v[:root_v]:
                        self.link(self.find(u), self.find(x))
                        if self.node_colors[x] == -1:
                            for y in self.graph[x]:
                                relevant_edges.append((x, y))
                            self.bridge[x] = v, w
                    for x in path_w[:root_w]:
                        self.link(self.find(u), self.find(x))
                        if self.node_colors[x] == -1:
                            for y in self.graph[x]:
                                relevant_edges.append((x, y))
                            self.bridge[x] = w, v
                    self.origin[self.find(u)] = u
        return aug_path 
    def find_max_matching(self):
        while True:
            # try to find augmenting path
            aug_path = self.find_augmenting_path()
            if not aug_path:
                # if we didn't we're done
                break
            # if we did, flip the matching along the path
            for u, v in zip(aug_path[::2], aug_path[1::2]):
                self.matching[u] = v
                self.matching[v] = u
        return self.matching

def solution(banana_list):
    # this is a maximum matching problem
    # first we need to construct the graph
    n = len(banana_list)
    graph = blossom(n)
    for u in range(n):
        for v in range(u + 1, n):
            a = banana_list[u]
            b = banana_list[v]
            if loops(a, b):
                graph.add_edge(u, v)
    # now we run the blossom algorithm
    mates = graph.find_max_matching()
    # and return the number of exposed vertices
    return mates.count(-1)

print solution([1, 1]) == 2
print solution([1, 7, 3, 21, 13, 19]) == 0
