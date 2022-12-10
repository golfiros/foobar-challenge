def gen_subsets(l):
    n = len(l)
    m = 2 ** n
    # skip the empty subset
    for i in range(1, m):
        include = [j for j in range(n) if (i >> j) % 2]
        yield [l[j] for j in include]
def solution(l):
    # to start we sort the list so that
    # we have the largest possible numbers
    # for the given set of digits
    l = sorted(l, reverse=True)
    # initialize our possibilities with 0
    number = 0
    # since L is so small we can probably
    # get away with iterating over every
    # subset
    for digits in gen_subsets(l):
        # to get the number we're looking at,
        # convert to string, concatenate everything,
        # and finally convert back to integer
        new_number = int(reduce(lambda x,y: x + y, map(str, digits)))
        if new_number % 3 == 0 and new_number > number:
            # this is a better choice
            number = new_number
    # return whatever the best number we found is
    return number

print solution([3, 1, 4, 1]) == 4311
print solution([3, 1, 4, 1, 5, 9]) == 94311
