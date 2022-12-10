# didn't save this one so i'm doing it again
# for completeness

def gen_primes():
    # generator via sieve of eratosthenes
    primes = set()
    n = 2
    while True:
        prime = True
        for p in primes:
            if n % p == 0:
                prime = False
                break
        if prime:
            primes.add(n)
            yield n
        n += 1

def solution(n):
    prime_string = ""
    prime_iterator = gen_primes()
    while len(prime_string) < n + 5:
        # generate as many primes as we need
        prime_string += str(next(prime_iterator))
    return prime_string[n:n+5]

print solution(0) == "23571"
print solution(3) == "71113"
