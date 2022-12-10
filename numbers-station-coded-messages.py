def solution(l, t):
    n = len(l)
    # pointer to keep track of the end of
    # the list being considered
    fast_pointer = 0
    # tally for sum of elements 
    # within the indicies
    total = 0
    # iterate over beggining of list
    for slow_pointer in range(n):
        # move the end forward until we bust
        while total < t and fast_pointer < n:
            total += l[fast_pointer]
            fast_pointer += 1
        # if we matched, we're done
        if total == t:
            return [slow_pointer, fast_pointer - 1]
        # if we overshot, pull back
        else:
            total -= l[slow_pointer]
    # if we haven't returned, there'se no solution
    return [-1, -1]

print solution([1, 2, 3, 4], 15) == [-1, -1]
print solution([4, 3, 10, 2, 8], 12) == [2, 3]
