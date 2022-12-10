def generalized_pentagonal_numbers():
    # generator for generalized pentagonal
    # numbers and their sign in the pentagonal
    # theorem
    k = 1
    sign = 1
    while True:
        yield sign, k * (3 * k - 1) / 2
        yield sign, k * (3 * k + 1) / 2
        k += 1
        sign *= -1

partitions_cache = {0 : 1}
def partitions(n):
    # generate the integer partitions via
    # Euler's pentagonal theorem
    if n in partitions_cache:
        return partitions_cache[n]
    out = 0
    for sign_k, g_k in generalized_pentagonal_numbers():
        m = n - g_k
        if m < 0:
            break
        out += sign_k * partitions(m)
    partitions_cache[n] = out
    return out

def strict_partitions(n):
    # slight variation on the pentagonal
    # theorem due to the bijection between
    # strict partitions and partitions with
    # only odd parts
    out = partitions(n)
    for sign_k, g_k in generalized_pentagonal_numbers():
        m = n - 2 * g_k
        if m < 0:
            break
        out += -sign_k * partitions(m)
    return out

def solution(n):
    # we just want to generate the number of
    # strict partitions of n, given in the 
    # OEIS A000009

    # we return the answer minus one, because
    # we don't want just a single tower instead
    # of a staircase
    return strict_partitions(n) - 1

print solution(3) == 1
print solution(200) == 487067745
