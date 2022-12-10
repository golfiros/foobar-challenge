# simple memoization
solution_cache = {1 : 0}
def solution(n):
    n = int(n)
    # pretty clear that dividing by 2
    # is always faster when its possible
    # we do all of them first to save on
    # recursion calls
    dist_even = 0
    while n % 2 == 0:
        n /= 2
        dist_even += 1
    # now we do recursion for whatever's
    # leftover
    if n in solution_cache:
        dist_odd = solution_cache[n]
    else:
        dist_odd = 1 + min(solution(n - 1), solution(n + 1))
        solution_cache[n] = dist_odd
    # and return total distance
    return dist_even + dist_odd

print solution("4") == 2
print solution("15") == 5
