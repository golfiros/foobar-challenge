def solution(n, b):
    k = len(n)

    # we start by implementing the iteration
    def iterate(m):
        # here m is a string corresponding 
        # to the number in base b
        m_sorted = map(int, sorted(m))
        # get x and y as actual integers
        x = 0
        y = 0
        pow = 1
        for i in range(k):
            x += pow * m_sorted[i]
            y += pow * m_sorted[k - 1 - i]
            pow *= b
        z = x - y
        # write z back as a string in base b
        z_string = ""
        for i in range(k):
            z_string = str(z % b) + z_string
            z /= b
        return z_string

    # and now we implement a tortoise and hare algorithm
    tortoise = iterate(n)
    hare = iterate(tortoise)

    while tortoise != hare:
        tortoise = iterate(tortoise)
        hare = iterate(iterate(hare))

    length = 1
    hare = iterate(tortoise)
    while tortoise != hare:
        hare = iterate(hare)
        length += 1

    return length

print solution("210022", 3) == 3
print solution("1211", 10) == 1
