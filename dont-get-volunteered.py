def to_coordinate(n):
    return (n % 8, n / 8)
    
offsets = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

def get_moves(p):
    base = []
    for d in offsets:
        base.append(tuple(map(lambda x, y: x + y, p, d)))
    output = []
    for m in base:
        if 0 <= m[0] <= 7 and 0 <= m[1] <= 7:
            output.append(m)
    return output
    
def distance(p, q):
    new_p = points_p = [p]
    new_q = points_q = [q]
    moves_p = [0]
    moves_q = [0]
    d = 0
    while True:
        points_c = set(points_p).intersection(points_q)
        if points_c:
            break
        d += 1
        new_p = [point for p0 in new_p for point in get_moves(p0) if point not in points_p]
        new_q = [point for q0 in new_q for point in get_moves(q0) if point not in points_q]
        points_p += new_p
        moves_p += [d] * len(new_p)
        points_q += new_q
        moves_q += [d] * len(new_q)
    moves_p = [moves_p[points_p.index(point)] for point in points_c]
    moves_q = [moves_q[points_q.index(point)] for point in points_c]
    dist = [a + b for a,b in zip(moves_p, moves_q)]
    return min(dist)
    
def solution(src, dest):
    return distance(to_coordinate(src), to_coordinate(dest))

print solution(19, 36) == 1
print solution(0, 1) == 3
