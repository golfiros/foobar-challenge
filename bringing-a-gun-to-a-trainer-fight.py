from fractions import gcd
from itertools import product

class Point:
    # simple helper class for arithmetic
    # on 2d points
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def norm(self):
        # extracts the norm of the vector given
        # by the point
        return self.x * self.x + self.y * self.y

    def reduced(self):
        # extracts the simplified direction of the point
        d = abs(gcd(self.x, self.y))
        if d == 0:
            return Point(0, 0)
        return Point(self.x / d, self.y / d)

    def to_tuple(self):
        return (self.x, self.y)

def reflect(initial, dimension, number):
    # finds the coordinate of reflecting "initial"
    # in a mirror of size "dimension" a total of 
    # "number" times
    return number * dimension + (initial if number % 2 == 0 else dimension - initial) 

def solution(dimensions, your_position, trainer_position, distance):
    sq_distance = distance * distance
    
    x_dim, y_dim = dimensions[0], dimensions[1]
    source = Point(your_position[0], your_position[1])
    target = Point(trainer_position[0], trainer_position[1])
    
    source_hits = {} 
    target_hits = {}

    def update_hits(hits, shot):
        # take note of the closest valid shot
        sq_dist = shot.norm()
        if sq_dist > sq_distance:
            return hits
        dir = shot.reduced().to_tuple()
        if dir in hits:
            hits[dir] = min(hits[dir], sq_dist)
        else:
            hits[dir] = sq_dist
        return hits
   
    def ellipse_iterator():
        # iterates over all possible reflections
        # the upper bounds for the pair m,n looks
        # like an ellipse
        m, n = 0, 0
        while x_dim * x_dim * m * (m - 4) <= sq_distance:
            while x_dim * x_dim * m * (m - 4) + y_dim * y_dim * n * (n - 4) <= sq_distance:
                for s,t in product((1,-1), repeat=2):
                    # iterate over signs 
                    # we waste a couple iterations for zeroes
                    # but that's fine
                    yield s * m, t * n
                n += 1
            n = 0
            m += 1
    
    for m, n in ellipse_iterator():
        source_r = Point(
                reflect(source.x, x_dim, m),
                reflect(source.y, y_dim, n)
                )
        target_r = Point(
                reflect(target.x, x_dim, m),
                reflect(target.y, y_dim, n)
                )
        
        source_shot = source_r - source
        target_shot = target_r - source

        source_hits = update_hits(source_hits, source_shot)
        target_hits = update_hits(target_hits, target_shot)

    count = 0
    for dir, sq_dist in target_hits.items():
        if dir in source_hits and source_hits[dir] < sq_dist:
            continue
        count += 1
    return count

print solution([3,2], [1,1], [2,1], 4) == 7
print solution([300,275], [150,150], [185,100], 500) == 9
