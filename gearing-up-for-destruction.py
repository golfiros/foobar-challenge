from fractions import Fraction as frac

def solution(pegs):
    n = len(pegs)
    # we take note of the distances between the pegs
    distance = map(lambda x: x[1] - x[0], zip(pegs, pegs[1:]))
    # we use a relationship between the first radius and the 
    # alternating sum of the distances derived from
    # radius[i] + radius[i + 1] = distance[i]
    # radius[0] = 2 * radius[n]
    radius = frac(2, 1 if n % 2 else 3) * (sum(distance[::2]) - sum(distance[1::2]))
    # if this gear is out of spec we're done
    if radius < 1:
        return [-1, -1]
    for i in range(n - 1):
        # now we iterate over the rest of the
        # pegs and if any of the gears are out
        # of spec we return a failure
        radius = distance[i] - radius
        if radius < 1:
            return [-1, -1]
    # we stopped at the last gear so we go back to 
    # the first and return
    radius = 2 * radius
    return [radius.numerator, radius.denominator]

print solution([4, 30, 50]) == [12, 1]
print solution([4, 17, 50]) == [-1, -1]
