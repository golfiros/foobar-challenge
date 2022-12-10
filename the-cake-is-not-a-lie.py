def match_length(s, i1, i2):
    # computes the lenght of matching prefixes
    # of s[i1:] and s[i2:]
    n = len(s)
    if i1 == i2:
        return n - i1
    count = 0
    while i1 < n and i2 < n and s[i1] == s[i2]:
        count +=1
        i1 += 1
        i2 += 1
    return count

def solution(s):
    # we start by running the preprocessing
    # step of Boyer--Moore on s without any prefixing
    n = len(s)
    # handle exceptionally small cakes
    if n < 2:
        return 1
    # we now construct the z-list such  
    # that s[i:i+z[i]] = s[:z[i]]

    # initializations
    z = [n, match_length(s, 0, 1)] + [0] * (n - 2)
    for i in range(2, 1 + z[1]):
        z[i] = z[1] - i + 1
    # bounds of substring we're looking at
    l = 0
    r = 0
    for i in range(2 + z[1], n):
        if i <= r:
            # i is within our substring
            k = i - l
            b = z[k]
            a = r - i + 1
            if b < a:
                # we are still on the same substring
                z[i] = b
            else:
                # we need to jump
                z[i] = a + match_length(s, a, r + 1)
                l = i
                r = i + z[i] - 1
        else:
            # we just jump and restart from where we are
            z[i] = match_length (s, 0, i)
            if z[i] > 0:
                l = i
                r = i + z[i] - 1
    # now we use this information to compute the period
    # iterate over divisors of n
    for i in (x for x in range(1, n) if n % x == 0):
        # if i+z[i] = n, that means 
        # s = s[:i]+s[i:i+z[i]]
        #   = s[:i]+s[:z[i]]
        #   ...
        #   = s[:z[i]] * (n / i)
        # so we found our period
        if i + z[i] == n:
            return n / i
    # if none of these work we just don't 
    # cut the cake at all
    return 1

print solution("abcabcabcabc") == 4
print solution("abccbaabccba") == 2
