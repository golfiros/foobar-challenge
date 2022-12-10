def beatty_sum(p, q, m):
    # simple base case
    if m == 0:
        return 0
    # here r ~ p/q is a sufficiently good approximation
    # assuming M = floor(m * r)
    # for s = r / (r - 1) ~ p/(p-q)
    # and n = floor(M / s) 
    #       = floor(m * (r - 1))
    # we have B_r(m) + B_s(n) = M * (M + 1) / 2
    # from https://en.wikipedia.org/wiki/Beatty_sequence
    
    # for convergence we must have n < m
    # which translates to r < 2 and can be implemented by
    # B_r(m) = B_{r-k}(m) + k * m * (m + 1) / 2
    
    # putting all of this together we get a recursion
    k = p / q - 1
    p = p - k * q
    M = m * p / q
    n = m * (p - q) / q
    return k * m * (m + 1) / 2 + M * (M + 1) / 2 - beatty_sum(p, p - q, n)

def refine(p, q):
    # rational approximations of sqrt2 via pell numbers
    return (p + 2 * q, p + q)
    
def solution(s):
    p, q = 1, 1 # sqrt2 ~ p/q
    m = int(s)
    N = 10 ** 100
    while q < N:
        # generate good approximation of sqrt2
        p, q = refine(p, q)
    return str(beatty_sum(p, q, m))

print solution("77") == "4208"
print solution("5") == "19"
