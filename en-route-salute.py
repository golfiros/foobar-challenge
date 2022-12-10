def solution(s):
    # an employee moving to the left
    # is going to salute all, but only
    # those moving to the right that are
    # to its left, and vice versa.

    # by symmetry we only need to tackle
    # one of the directions

    # we keep a tally of right movers up
    # to a certain point
    right_moving = 0

    # and therefore the number of salutes
    # the left movers are going to perform
    salutes_left = 0
    for char in s:
        if char == ">":
            right_moving += 1
        if char == "<":
            salutes_left += right_moving

    #by symmetry we multiply by 2 and return
    return 2 * salutes_left

print solution(">----<") == 2
print solution("<<>><") == 4
