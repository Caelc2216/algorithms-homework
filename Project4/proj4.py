# Cael Church
# September 23 2026
# Advanced Algorithms


# Part 1
def OptCost(start, end, frequencies=None):
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


# Part 2
def OptCost_ref(start, end, frequencies):
    def OptCost2(start, end):
        sum = 0
        if start==end:
            return 0
        else:
            for i in range(start, end):
                sum += frequencies[i]
        for j in range(start, end):
            if j==start:
                best = OptCost2(start, j) + OptCost2(j+1, end)
            else:
                best = min(OptCost2(start, j) + OptCost2(j+1, end), best)
        return sum + best
    return OptCost2(start, end)




def test_OptCost_ref_baseCase():
    frequencies = [10]
    assert OptCost_ref(0,1,frequencies) == 10

def test_OptCost_ref_baseCase2():
    frequencies = [10, 1]
    assert OptCost_ref(0,2,frequencies) == 12

def test_OptCost_ref_threeKeys_uniform():
    frequencies = [1, 1, 1]
    assert OptCost_ref(0, 3, frequencies) == 5

def test_OptCost_ref_threeKeys_notuniform():
    frequencies = [2, 3, 1]
    assert OptCost_ref(0, 3, frequencies) == 9


# Part 3
def CombineCostsAndTrees(root_and_cost, left_and_cost, right_and_cost):
    root = root_and_cost[0]
    rootCost = root_and_cost[1]
    left = left_and_cost[1]
    leftCost = left_and_cost[0]
    right = right_and_cost[1]
    rightCost = right_and_cost[0]
    return (rootCost + leftCost + rightCost, (root, left, right))

def OptCostAndTree(start, end, frequencies):
    rootCost = 0
    if start == end:
        return 0, ()
    else:
        for i in range(start, end):
            rootCost += frequencies[i]
        for j in range (start, end):
            if j==start:
                best = (CombineCostsAndTrees((j, rootCost), OptCostAndTree(start, j, frequencies), OptCostAndTree(j+1, end, frequencies)))
            else:
                result1 = (CombineCostsAndTrees((j, rootCost), OptCostAndTree(start, j, frequencies), OptCostAndTree(j+1, end, frequencies)))
                best = result1 if result1[0] < best[0] else best
    return best


def test_OptCostAndTree_singleKey():
    frequencies = [10]
    cost, tree = OptCostAndTree(0, 1, frequencies)
    assert cost == 10
    assert tree == (0, (), ())

def test_OptCostAndTree_twoKeys():
    frequencies = [10, 1]
    cost, tree = OptCostAndTree(0, 2, frequencies)
    assert cost == 12
    assert tree == (0, (), (1, (), ()))
def test_OptCostAndTree_threeKeys_uniform():
    frequencies = [1, 1, 1]
    cost, tree = OptCostAndTree(0, 3, frequencies)
    assert cost == 5
    assert tree == (1, (0, (), ()), (2, (), ()))

def test_OptCostAndTree_threeKeys_skewed():
    frequencies = [2, 3, 1]
    cost, tree = OptCostAndTree(0, 3, frequencies)
    assert cost == 9
    assert tree == (1, (0, (), ()), (2, (), ()))

# Part 4
def OptCostWithLeftCost(start, end, frequencies, leftCost):
    partialSum = 0
    if start==end:
        return 0
    else:
        for i in range(start, end):
            partialSum += frequencies[i]
    for j in range(start, end):
        left = OptCostWithLeftCost(start, j, frequencies, leftCost)
        if j - start > 0:
            left += leftCost * sum(frequencies[start:j])
        right = OptCostWithLeftCost(j+1, end, frequencies, leftCost)
        if j==start:
            best = left + right
        else:
            best = min(left + right, best)

    return partialSum + best


def test_OptCostWithLeftCost_baseCase():
    frequencies = [10]
    assert OptCostWithLeftCost(0,1,frequencies, 2) == 10

def test_OptCostWithLeftCost_baseCase2():
    frequencies = [10, 1]
    assert OptCostWithLeftCost(0,2,frequencies, 2) == 12

def test_OptCostWithLeftCost_threeKeys_uniform():
    frequencies = [1, 1, 1]
    assert OptCostWithLeftCost(0, 3, frequencies, 2) == 6

def test_OptCostWithLeftCost_threeKeys_notuniform():
    frequencies = [2, 3, 1]
    assert OptCostWithLeftCost(0, 3, frequencies, 2) == 11



# Part 5
def OptCostAndTreeWithLeftCost(start, end, frequencies, leftCost):
    rootCost = 0
    if start == end:
        return 0, ()
    else:
        for i in range(start, end):
            rootCost += frequencies[i]
        for j in range (start, end):
            left = OptCostAndTreeWithLeftCost(start, j, frequencies, leftCost)
            right = OptCostAndTreeWithLeftCost(j+1, end, frequencies, leftCost)
            if j-start > 0:
                left = left[0] + leftCost * sum(frequencies[start:j]), left[1]
            if j==start:
                best = (CombineCostsAndTrees((j, rootCost), left, right))
            else:
                result1 = (CombineCostsAndTrees((j, rootCost), left, right))
                best = result1 if result1[0] < best[0] else best
    return best


def test_OptCostAndTreeWithLeftCost_singleKey():
    frequencies = [10]
    cost, tree = OptCostAndTreeWithLeftCost(0, 1, frequencies, 2)
    assert cost == 10
    assert tree == (0, (), ())

def test_OptCostAndTreeWithLeftCost_twoKeys():
    frequencies = [10, 1]
    cost, tree = OptCostAndTreeWithLeftCost(0, 2, frequencies, 2)
    assert cost == 12
    assert tree == (0, (), (1, (), ()))
def test_OptCostAndTreeWithLeftCost_threeKeys_uniform():
    frequencies = [1, 1, 1]
    cost, tree = OptCostAndTreeWithLeftCost(0, 3, frequencies, 2)
    assert cost == 6
    assert tree == (0, (), (1, (), (2, (), ())))

def test_OptCostAndTreeWithLeftCost_threeKeys_skewed():
    frequencies = [2, 3, 1]
    cost, tree = OptCostAndTreeWithLeftCost(0, 3, frequencies, 2)
    assert cost == 11
    assert tree == (0, (), (1, (), (2, (), ())))