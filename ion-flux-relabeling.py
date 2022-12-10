# another one i didn't save, doing it again

def solution(h, q):
    root_node = 2 ** h - 1 
    out = []
    for node in q:
        # if we're looking at the root we just add -1
        if node == root_node:
            out.append(-1)
            continue
        # for other nodes it's a little more interesting
        # we start at the root
        curr_node = root_node
        # and realize that the left and right child
        # trees are identical up to an offset equal
        # to the value of the left child

        #    7
        #  3   6
        # 1 2 4 5

        # and this holds recursively as we go into
        # the left child
        
        # so instead of actually keeping track of our
        # branching, every time we move into the right
        # child, we actually move into the left child
        # and add an offset, removing this same offset
        # from the target node to keep things consistent
        offset = 0
        while True:
            right_child = curr_node - 1
            left_child = right_child / 2
            # if our node is one of the children we're done
            if node == right_child or node == left_child:
                out.append(offset + curr_node)
                break
            # otherwise branch
            if node > left_child:
                offset += left_child
                node -= left_child
            curr_node = left_child
        
    return out

print solution(3, [1, 4, 7]) == [3, 6, -1]
print solution(3, [7, 3, 5, 1]) == [-1, 7, 6, 3]
print solution(5, [19, 14, 28]) == [21, 15, 29]
