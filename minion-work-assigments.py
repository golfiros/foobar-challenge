from collections import Counter

def solution(data, n):
    # count how many of each element 
    # appears in the list
    counts = Counter(data)
    for i, id in enumerate(data):
        if counts[id] > n:
            # if we go over the allowed count
            # we replace the element with -1
            # to filter it out later
            data[i] = -1
    return [x for x in data if x != -1]

print solution([1, 2, 3], 0) == []
print solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1) == [1, 4]
