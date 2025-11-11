def has_adjacent_duplicate(L):
    if len(L)<2:
        return False
    prev=0
    for number in L:
        if number==prev:
            return True
        prev=number
    return False