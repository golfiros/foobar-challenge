from fractions import gcd
from fractions import Fraction as frac

def gauss_elim(A):
    m = len(A)
    n = len(A[0])
    h = k = 0
    while h < m and k < n: # row echelon form
        abs_row = [abs(A[i][k]) for i in range(h, m)]
        ii = h + abs_row.index(max(abs_row))
        if A[ii][k] == 0:
            k += 1
            continue
        A[h], A[ii] = A[ii], A[h]
        for i in range(h + 1, m):
            A[i] = map(lambda x,y: x - y * frac(A[i][k], A[h][k]), A[i], A[h])
        h += 1
        k += 1
    for h in reversed(range(m)): # reduce rows
        l = filter(lambda x: x != 0, A[h])
        if not l:
            continue
        k = A[h].index(l[0])
        for i in range(0, h):
            A[i] = map(lambda x,y: x - y * frac(A[i][k], A[h][k]), A[i], A[h])
        A[h] = map(lambda x: x / A[h][k], A[h])
    return A
    
def identity(A): # returns "identity" with same shape as A
    return [[1 if j == i else 0 for j in range(len(A[0]))] for i in range(len(A))]

def subtract(A, B): # returns A - B
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
def augment(A, B): # concatenates B to the right of A
    return [A[i] + B[i] for i in range(len(A))]

def solution(m):
    # just solve for the absorbing probabilities
    # of the given absorbing markov chain
    # https://en.wikipedia.org/wiki/Absorbing_Markov_chain
    sums = [sum(row) for row in m]
    transient = [i for i,s in enumerate(sums) if s > 0]
    absorbing = [i for i,s in enumerate(sums) if s == 0]
    n_t = len(transient)
    n_a = len(absorbing)
    # special case for initial state being absorbing
    if sums[0] == 0:
        return [1] + [0] * (n_a - 1) + 1
    Q = [[frac(m[i][j],sums[i]) for j in transient] for i in transient]
    R = [[frac(m[i][j],sums[i]) for j in absorbing] for i in transient]
    N_inv = subtract(identity(Q), Q)
    IcB =  gauss_elim(augment(N_inv, R))
    p = IcB[0][n_t : n_t + n_a] + [1]
    return map(lambda x: int(x / reduce(gcd, p)), p)

print solution([[0, 2, 1, 0, 0],
                [0, 0, 0, 3, 4],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
                ]) == [7, 6, 8, 21]

print solution([[0, 1, 0, 0, 0, 1],
                [4, 0, 0, 3, 2, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
                ]) == [0, 3, 2, 9, 14] 
