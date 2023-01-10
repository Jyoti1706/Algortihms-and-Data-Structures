def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    next_idx = (currentIdx+jump)%len(array)
    if next_idx >= 0:
        return next_idx
    else:
        return len(array)+next_idx


def hasSingleCycle(array):
    n = len(array)
    numElementVisited=0
    currentIdx = 0
    while numElementVisited < len(array):
        if numElementVisited > 0 and currentIdx == 0:
            return False
        numElementVisited += 1
        currentIdx = getNextIdx(currentIdx,array)
    return currentIdx == 0

print(hasSingleCycle([2, 3, 1, -4, -4, 2]))