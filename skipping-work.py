import heapq
def solution(x, y):
    # get which of the lists has the extra member
    short, long = min((x, y), key = len), max((x, y), key = len) 
    # sort the lists into a heap
    heapq.heapify(short)
    heapq.heapify(long)
    # pop until we get different smaller elements
    # or we run out of the smaller list
    while short and short[0] == long[0]:
        heapq.heappop(short)
        heapq.heappop(long)
    # return the smallest element of the long list
    return long[0]

print solution([13, 5, 6, 2, 5], [5, 2, 5, 13]) == 6
print solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]) == -4
