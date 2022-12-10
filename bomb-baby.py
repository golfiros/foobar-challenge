def solution(x, y):
    s = 0
    m = int(x)
    f = int(y)
    while True:
        if m == 1 and f == 1:
            return str(s)
        if m > f:
            if f == 1:
                s += m - 1
                m = 1
                continue
            s += m / f
            m %= f
        else:
            if m == 1:
                s += f - 1
                f = 1
                continue
            s += f / m
            f %= m
        if m < 1 or f < 1:
            return "impossible"

print solution("2", "1") == "1"
print solution("4", "7") == "4"
