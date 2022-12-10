# it took me over a week to work out the math for this
# i made a writeup for everything i used since i don't
# think i could reasonably explain it in code comments
# https://golfiros.github.io/disorderly_escape.pdf

def gen_partitions(n):
    # generator for partitions in reverse lexicographic order
    part = [0] * (n + 1)
    k = 1
    s = n - 1
    while k != 0:
        x = part[k - 1] + 1
        k -= 1
        while 2 * x <= s:
            part[k] = x
            s -= x
            k += 1
        l = k + 1
        while x <= s:
            part[k] = x
            part[l] = s
            yield part[:k + 2]
            x += 1
            s -= 1
        part[k] = x + s
        s = x + s - 1
        yield part[:k + 1]
        
def count_entries(part):
    # implementation of c_p(lambda)
    c_part = [0] * part[-1]
    s_part = part + [-1]
    k = 0
    n = 0
    while k < len(c_part):
        while s_part[n] == k + 1:
            n += 1
            c_part[k] += 1
        k += 1
    return c_part
        
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
    
def conj_class_size_den(c_part):
    # implementation of N(lambda)
    return reduce(lambda x, y: x * (y[0] + 1) ** y[1] * factorial(y[1]), enumerate(c_part), 1)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def partition_product(pm, pn):
    # implementation of * product
    c = []
    for x in pm:
        for y in pn:
            d = gcd(x, y)
            c += [x * y / d] * d
    return sorted(c)

def solution(w, h, s):
    m = w
    n = h
    r = s
    fact_m = factorial(m)
    fact_n = factorial(n)
    t = 0
    # just going over burnside's lemma
    for part_m in gen_partitions(m):
        counts_m = count_entries(part_m)
        mult_m = fact_m / conj_class_size_den(counts_m)
        for part_n in gen_partitions(n):
            counts_n = count_entries(part_n)
            mult_n = fact_n / conj_class_size_den(counts_n)
            part_mn = partition_product(part_m, part_n)
            counts = count_entries(part_mn)
            cycles = sum(counts)
            t += mult_m * mult_n * r ** cycles
    return str(t / (fact_m * fact_n))

print solution(2, 3, 4) == "430"
print solution(2, 2, 2) == "7"
