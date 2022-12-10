from itertools import combinations

def solution(num_buns, num_required):
    out = [[] for i in range(num_buns)]
    # generate who has each key
    # make sure (num_required - 1) don't have it
    # and that each goes to a different set of bunnies
    sets = [list(s) for s in combinations(range(num_buns), num_buns - (num_required - 1))]
    # populate the output
    for key, bunnies in enumerate(sets):
        for bunny in bunnies:
            out[bunny].append(key)
    return out

print solution(2, 1) == [[0], [0]]
print solution(5, 3) == [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]
print solution(4, 4) == [[0], [1], [2], [3]]
