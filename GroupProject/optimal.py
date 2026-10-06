





# Part 1
# 1. Opt_Cost(frewuencies, cost_per_rotation, move_cost_per_distance, cost_per_scan) would return the optimal cost given the params
# 2. computing the optimal cost of the left and right sides of a tree given a root node. The parameters would be starting node, and ending node.
# 3. The top level function will keep the min cost of each recursive call and return the min_cost
# 4. 


# Part 2
def optimal_cost_backtracking(frequencies, cost_per_rotation, move_cost_per_distance, cost_per_scan):
    cheapest = float('inf')

    def branch_cost(start, end):
        sum = 0
        if start==end:
            return 0
        else:
            for i in range(start, end):
                # for root
                cost_to_move = i * move_cost_per_distance * 2
                if i != 0:
                    cost_to_rotate = cost_per_rotation * 2
                else: 0
                sum += (cost_to_move + cost_to_rotate + cost_per_scan) * frequencies[i] 
            
        for j in range(len(end-start)):
            left = branch_cost[0, j-1]
            right = branch_cost(j+1, len(end-start)-1)
        return None

# if root_index == 0:
#     cost_to_move_and_scan_root = cost_per_scan
# else:
#     cost_to_move_and_scan_root = root_index * move_cost_per_distance +  cost_per_scan
# distance_from_root = absolute_value|root_index - current_index|
# add cost_per_rotation
    








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