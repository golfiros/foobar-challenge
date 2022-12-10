from math import sqrt, floor

def solution(area):
    out = []
    # just a greedy algorithm
    while area > 0:
        length = int(floor(sqrt(area)))
        panel = length * length
        area -= panel
        out += [panel]
    return out

print solution(15324) == [15129,169,25,1]
print solution(12) == [9,1,1,1]
