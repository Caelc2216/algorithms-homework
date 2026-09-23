
def OptCost(start, end, frequencies):
    sum = 0
    if start==end:
        return 0
    else:
        for i in range(start, end):
            sum += frequencies[i]
    for j in range(start, end):
        if j==start:
            best = OptCost(start, j, frequencies) + OptCost(j+1, end, frequencies)
        else:
            best = min(OptCost(start, j, frequencies) + OptCost(j+1, end, frequencies), best)

    return sum + best

def test_OptCost_baseCase():
    frequencies = [10]
    assert OptCost(0,1,frequencies) == 10

def test_OptCost_baseCase2():
    frequencies = [10, 1]
    assert OptCost(0,2,frequencies) == 12

def test_OptCost_threeKeys_uniform():
    frequencies = [1, 1, 1]
    assert OptCost(0, 3, frequencies) == 5

def test_OptCost_threeKeys_notuniform():
    frequencies = [2, 3, 1]
    assert OptCost(0, 3, frequencies) == 9