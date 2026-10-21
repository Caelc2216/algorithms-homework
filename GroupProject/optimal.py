# Cael Church
# 10/9/26

# I worked on this project alone as I thought in class it was said that working in a group was optional

from functools import cache



# Part 1
# 1. Opt_Cost(frequencies, cost_per_rotation, move_cost_per_distance, cost_per_scan) would return the minimal cost that is found by trying all possible root combinations and weighting the move, rotation, and scan costs.
# 2. computing the optimal cost of the left and right sides of a tree given a root node. The parameters would be starting node, ending node, the parent node/where we are coming from, and what direction we are facing. we need these additional parameters since every time the robot moves it comes from the previous root node, and there is a rotation cost associated with switching directions
# 3. The top level function starts at index 0 and with the robot facing left, it gives us our original starting point where the rest of the code is based off of, it also provides the costs and frequencies of each node. 
# 4a. The base case is when the starting node is the same as the ending node.
# 4b. It should return 0 because we are excluding end in our loop. End is beyond the length of our frequencies, meaning there would be no calls to end because it doesn't exist
# 5a. The solution of the nested function will compute the cost for a given span by combining the cost of the root node with its subsequent branches
# 5b. It will consider what moves, scans, and rotations it needs to take as a root node. Since every scan needs to go to the root node first this needs to be efficient as the cost will be multiplied by every node in the given span
# 5c. It will recurse on the left and right branches passing in itself as the parent node and which direction the robot is facing so that it can find the efficient node for its span
# 5d. It will compare the smallest cost candidate with each candidate solution and keep the one with the smallest cost 


# Part 2
def optimal_cost_backtracking(frequencies, cost_per_rotation, move_cost_per_distance, cost_per_scan):

    def branch_cost(start, end, moving_from, facing_right):
        cheapest = float('inf')
        sum = 0
        if start==end:
            return 0
        else:
            for node in range(start, end):
                sum += frequencies[node]
            for i in range(start, end):
                newDirection = facing_right
                return_cost = 0

                # needs to switch direction
                if (facing_right and i < moving_from) or (not facing_right and i > moving_from):
                    newDirection = not facing_right
                    cost = ((abs(i-moving_from) * move_cost_per_distance) + cost_per_scan + (cost_per_rotation)) * sum
                else:
                    cost = (abs(i-moving_from) * move_cost_per_distance + cost_per_scan) * sum

                # needs to switch direction to go back
                if newDirection:
                    return_cost = ((i * move_cost_per_distance) + cost_per_rotation) * frequencies[i]
                else:
                    return_cost = (i * move_cost_per_distance * frequencies[i])
                cost = cost + return_cost
                left = branch_cost(start, i, i, newDirection)
                right = branch_cost(i+1, end, i, newDirection)
                cheapest = min(cost + left + right, cheapest)
        return cheapest
    return branch_cost(0, len(frequencies), 0, False)


# Part 3
def optimal_cost_memoized(frequencies, cost_per_rotation, move_cost_per_distance, cost_per_scan):

    @cache
    def branch_cost(start, end, moving_from, facing_right):
        cheapest = float('inf')
        sum = 0
        if start==end:
            return 0
        else:
            for node in range(start, end):
                sum += frequencies[node]
            for i in range(start, end):
                newDirection = facing_right
                return_cost = 0

                # needs to switch direction
                if (facing_right and i < moving_from) or (not facing_right and i > moving_from):
                    newDirection = not facing_right
                    cost = ((abs(i-moving_from) * move_cost_per_distance) + cost_per_scan + (cost_per_rotation)) * sum
                else:
                    cost = (abs(i-moving_from) * move_cost_per_distance + cost_per_scan) * sum

                # needs to switch direction to go back
                if newDirection:
                    return_cost = ((i * move_cost_per_distance) + cost_per_rotation) * frequencies[i]
                else:
                    return_cost = (i * move_cost_per_distance * frequencies[i])
                cost = cost + return_cost
                left = branch_cost(start, i, i, newDirection)
                right = branch_cost(i+1, end, i, newDirection)
                cheapest = min(cost + left + right, cheapest)
        return cheapest
    return branch_cost(0, len(frequencies), 0, False)


# Part 4
def optimal_tree(frequencies, cost_per_rotation, move_cost_per_distance, cost_per_scan):

    @cache
    def branch_cost(start, end, moving_from, facing_right):
        cheapest = float('inf'), ()
        sum = 0
        if start==end:
            return 0, ()
        else:
            for node in range(start, end):
                sum += frequencies[node]
            for i in range(start, end):
                newDirection = facing_right
                return_cost = 0

                # needs to switch direction
                if (facing_right and i < moving_from) or (not facing_right and i > moving_from):
                    newDirection = not facing_right
                    cost = ((abs(i-moving_from) * move_cost_per_distance) + cost_per_scan + (cost_per_rotation)) * sum
                else:
                    cost = (abs(i-moving_from) * move_cost_per_distance + cost_per_scan) * sum

                # needs to switch direction to go back
                if newDirection:
                    return_cost = ((i * move_cost_per_distance) + cost_per_rotation) * frequencies[i]
                else:
                    return_cost = (i * move_cost_per_distance * frequencies[i])
                cost = cost + return_cost
                left = branch_cost(start, i, i, newDirection)
                right = branch_cost(i+1, end, i, newDirection)
                if (cost + left[0] + right[0]) < cheapest[0]:
                    cheapest = (cost + left[0] + right[0]), (i, left[1], right[1])
        return cheapest
    return branch_cost(0, len(frequencies), 0, False)








# Tests
# (frequencies, rotation, move, scan, optimal cost, optimal tree)
# Each case has exactly one optimal tree, so the tree is safe to check.
OPTIMAL_BST_CASES = [
    ([5],                3, 1, 2,   10, (0, (), ())),
    ([4, 3],             3, 1, 2,   44, (0, (), (1, (), ()))),
    ([4, 30],            3, 1, 2,  348, (1, (0, (), ()), ())),
    ([1, 1, 1],          3, 1, 2,   30, (0, (), (1, (), (2, (), ())))),
    ([4, 3, 28, 100, 5], 3, 1, 2, 2072, (3, (2, (1, (0, (), ()), ()), ()), (4, (), ()))),
    ([1, 1, 1, 1, 1, 50], 7, 2, 1, 1940,
     (5, (4, (3, (2, (1, (0, (), ()), ()), ()), ()), ()), ())),
    ([3, 1, 4, 1, 5, 9, 2, 6], 5, 2, 3, 1132,
     (2, (1, (0, (), ()), ()),
         (5, (4, (3, (), ()), ()), (7, (6, (), ()), ())))),
    ([20, 5, 1, 1, 30, 2, 2, 40], 4, 1, 0, 1512,
     (0, (), (1, (), (2, (), (3, (), (4, (), (5, (), (6, (), (7, (), ()))))))))),
]

# Fifty bins. Only a memoized solution finishes this one -- plain backtracking would
# have to look at more trees than there are atoms in anything you care about.
FIFTY_BIN_FREQUENCIES = (4, 3, 28, 100, 5) * 10
FIFTY_BIN_COST = 96532


def test_backtracking_finds_the_optimal_cost():
    for frequencies, rotation, move, scan, cost, tree in OPTIMAL_BST_CASES:
        assert cost == optimal_cost_backtracking(
            frequencies, cost_per_rotation=rotation, move_cost_per_distance=move, cost_per_scan=scan
        ), frequencies


def test_memoized_finds_the_same_costs():
    for frequencies, rotation, move, scan, cost, tree in OPTIMAL_BST_CASES:
        assert cost == optimal_cost_memoized(
            frequencies, cost_per_rotation=rotation, move_cost_per_distance=move, cost_per_scan=scan
        ), frequencies


def test_memoized_handles_fifty_bins():
    assert FIFTY_BIN_COST == optimal_cost_memoized(
        list(FIFTY_BIN_FREQUENCIES), cost_per_rotation=3, move_cost_per_distance=1, cost_per_scan=2)


def test_optimal_tree_and_its_cost():
    for frequencies, rotation, move, scan, cost, tree in OPTIMAL_BST_CASES:
        assert (cost, tree) == optimal_tree(
            frequencies, cost_per_rotation=rotation, move_cost_per_distance=move, cost_per_scan=scan
        ), frequencies


def test_optimal_tree_still_works_on_fifty_bins():
    frequencies = list(FIFTY_BIN_FREQUENCIES)
    cost, tree = optimal_tree(
        frequencies, cost_per_rotation=3, move_cost_per_distance=1, cost_per_scan=2)
    assert FIFTY_BIN_COST == cost
    # every bin appears exactly once, and the tree is a search tree on the bin numbers
    def bins_in_order(t):
        return [] if t == () else bins_in_order(t[1]) + [t[0]] + bins_in_order(t[2])
    assert list(range(len(frequencies))) == bins_in_order(tree)


if __name__ == "__main__":
    # Runs the tests without pytest, so you can step through them in a debugger.
    for test in [test_backtracking_finds_the_optimal_cost,
                 test_memoized_finds_the_same_costs,
                 test_memoized_handles_fifty_bins,
                 test_optimal_tree_and_its_cost,
                 test_optimal_tree_still_works_on_fifty_bins]:
        test()
        print("passed:", test.__name__)