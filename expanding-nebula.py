infinity = 1000 # larger than the number of entries in the past grid

# "low level" implementation of OBDDs as simulated pointers
# to "structs", so that only cheap integer operations are done

# if done in a strong typed language this could be made  
# safer with typedefing these pointers, but we're fine
nodes = [(infinity, 0, 0), (infinity,1, 0)]

# we make copious use of caching to skip calculations we've
# already done, significantly reducing problem complexity

node_cache = {(infinity, 0, 0): 0, (infinity, 1, 0): 1}
def node(v, t, f):
    # returns the ROBDD
    
    #   v
    #  / \
    # t   f
    
    # constructing it only if necessary
    global n_nodes
    if t == f:
        return t
    if (v, t, f) in node_cache:
        return node_cache[(v, t, f)]
    obdd = len(nodes)
    nodes.append((v, t, f))
    node_cache[(v, t, f)] = obdd
    return obdd

cond_cache = {}
def condition(obdd, v0, b):
    # returns the ROBDD of obdd after setting v0 to b
    node = nodes[obdd]
    if node[0] > v0:
        return obdd
    if node[0] == v0:
        return node[1] if b else node[2]
    if (obdd, v0, b) in cond_cache:
        return cond_cache[(obdd, v0, b)]
    n = node(node[0], condition(node[1], v0, b), condition(node[2], v0, b))
    cond_cache[(obdd, v0, b)] = n
    return n

conj_cache = {}
def conjoin(obdd1, obdd2):
    # returns the ROBDD of obdd1 & obdd2
    node1 = nodes[obdd1]
    node2 = nodes[obdd2]
    if node1[0] == infinity and node2[0] == infinity:
        return node1[1] and node2[1]
    if (obdd1, obdd2) in conj_cache:
        return conj_cache[(obdd1, obdd2)]
    v = min(node1[0], node2[0])
    n = node(v, conjoin(condition(obdd1, v, True), condition(obdd2, v, True)), conjoin(condition(obdd1, v, False), condition(obdd2, v, False)))
    conj_cache[(obdd1, obdd2)] = n
    return n

def dnc_conjoin(obddlist):
    # simple divide and conquer application of conjoin()
    x = len(obddlist)
    if x == 1:
        return obddlist[0]
    if x == 2:
        return conjoin(obddlist[0], obddlist[1])
    return conjoin(dnc_conjoin(obddlist[: x / 2]), dnc_conjoin(obddlist[x / 2 : x]))

count_cache = {}
def model_count(obdd, n):
    # counts the number of solutions to obdd=True given n free variables
    node = nodes[obdd]
    if node[0] == infinity:
        return 2 ** n if obdd else 0
    if (obdd, n) in count_cache:
        return count_cache[(obdd, n)]
    c = model_count(node[1], n - 1) + model_count(node[2], n - 1)
    count_cache[(obdd, n)] = c
    return c

def gen_obdd(x, a, b):
    # generate the OBDD for a given
    # combination of four grid elements
    
    # generates the following ROBDD
    
    #     0
    #    / \
    #   1   1
    #  / \ / \
    # b   2   2
    #    / \ / \
    #   b   3   3
    #      / \ / \
    #     b   a   b
    x1 = node(x[3], b, a)
    x2 = node(x[3], a, b)
    x3 = node(x[2], b, x1)
    x4 = node(x[2], x1, x2)
    x5 = node(x[1], b, x3)
    x6 = node(x[1], x3, x4)
    return node(x[0], x5, x6)
    
def chain_obdd(ind, obdd, b):
    # by a convenient indexing of the grid we can skip some
    # expensive conjoin operations by direct construction of
    # the conjoined ROBDDs for next-to-nearest neighbors
    if b:
        return gen_obdd(ind, obdd, 0)
    return gen_obdd(ind, 0, obdd)

def solution(g):
    h = len(g)
    w = len(g[0])
    # start with trivially true OBDDS
    even_obdds = [1] * h
    odd_obdds = [1] * h
    
    # we label the variables in the past grid as
    #  0   h+1  ...  wh+1 
    #  1   h+2  ...  wh+2
    # ...  ...  ...  ...
    #  h    2h  ... (w+1)h
    
    for j in reversed(range(w)):
        for i in range(h):
            ind = [(h + 1) * (j + 0) + i + 0,
                   (h + 1) * (j + 0) + i + 1,
                   (h + 1) * (j + 1) + i + 0,
                   (h + 1) * (j + 1) + i + 1]
            # do trivial conjoins of odd and even colums
            if j % 2 == 0:
                    even_obdds[i] = chain_obdd(ind, even_obdds[i], g[i][j])
            else:
                    odd_obdds[i] = chain_obdd(ind, odd_obdds[i], g[i][j])
    even = dnc_conjoin(even_obdds)
    odd = dnc_conjoin(odd_obdds)
    return model_count(conjoin(even, odd), (h + 1) * (w + 1))

print solution([[True, True, False, True, False, True, False, True, True, False],
                [True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, False, False, False, True],
                [False, True, False, False, False, False, True, True, False, False]
                ]) == 11567

print solution([[True, False, True],
                [False, True, False],
                [True, False, True]
                ]) == 4

print solution([[True, False, True, False, False, True, True, True],
                [True, False, True, False, False, False, True, False],
                [True, True, True, False, False, False, True, False],
                [True, False, True, False, False, False, True, False],
                [True, False, True, False, False, True, True, True]
                ]) == 254
