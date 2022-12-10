def to_tuple(s):
    return tuple(map(int, s.split(".")))

def solution(l):
    # we abuse python's built in tuple comparisons
    # since they do exactly what we want
    return sorted(l, key=to_tuple)

print solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]) == ["0.1","1.1.1","1.2","1.2.1","1.11","2","2.0","2.0.0"]
print solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]) == ["1.0","1.0.2","1.0.12","1.1.2","1.3.3"]
