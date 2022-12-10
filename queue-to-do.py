# forgot to push this one cause it wasn't saved either
# i remember implementing this exact logic
# and it failed tests

# i then did it in java and it worked

# here's python for consistency though
def solution(start, length):
    n = 0
    for i in range(length):
        for j in range(length - i):
            n ^= start + length * j + i
    return n

print solution(0, 3) == 2
print solution(17, 4) == 14
