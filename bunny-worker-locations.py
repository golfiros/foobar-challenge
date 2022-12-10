def solution(x, y):
    # this is just the standard bijection
    # C : N^2 -> N given by the Cantor 
    # pairing function
    return str(x + (x + y - 2) * (x + y - 1) / 2)

print solution(3, 2) == "9"
print solution(5, 10) == "96"
