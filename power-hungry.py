def solution(xs):
    n = len(xs)
    if n == 1:
        # if there's only one panel
        # we just return that
        return str(xs[0])
    # separate the panels by their signs
    # and flip the signs of negative panels
    # while sorting so that larger ones go
    # to the end
    positive_panels = [p for p in xs if p > 0]
    negative_panels = sorted([-p for p in xs if p < 0])
    
    # while there exists a negative pair we
    # move them over to the positives
    while len(negative_panels) > 1:
        positive_panels.append(negative_panels.pop())
        positive_panels.append(negative_panels.pop())

    if not positive_panels:
        # if don't have any positives that means
        # the initial state was a bunch of zeroes
        # and zero or one negative so we just return 0
        return str(0)

    # just return the product of the positive panels
    return str(reduce(lambda x, y: x * y, positive_panels))

print solution([2, 0, 2, 2, 0]) == "8"
print solution([-2, -3, 4, -5]) == "60"
