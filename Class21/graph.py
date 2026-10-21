# count_paths(graph, s, t) returns how many different paths go from s to t in
# a DAG, where graph maps each vertex to the list of vertices its edges point
# to. (In the graph g below, a reaches e by a-b-d-e and by a-c-d-e.)

from functools import cache
def count_paths(graph, s, t):
    @cache
    def num_paths_from(start):
        count = 0
        if (t == start):
            count += 1
            return count
        for i in range(len(graph[start])):
            if (graph[start][i] is not None):
                count += num_paths_from(graph[start][i])
        return count
    return num_paths_from(s)


# Write it so that this pytest test passes in O(V + E) time:
g = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": ["e"], "e": []}


def test_count_paths():
    assert count_paths(g, "a", "e") == 2
    assert count_paths(g, "b", "e") == 1
    assert count_paths(g, "e", "a") == 0
    ladder = {i: [i + 1, i + 2] for i in range(60)} | {60: [], 61: []}
    assert count_paths(ladder, 0, 60) == 2504730781961


# If you get done early, write topo_order(graph), which returns a list of all
# the vertices of a DAG in an order where every edge points forward. Make this
# pass, also in O(V + E) time:

def topo_order(dag):
    post_order = []
    visited = set()

    def build_topo_from(node):
        visited.add(node)
        for child in dag[node]:
            if child not in visited:
                build_topo_from(child)
        post_order.append(node)

    for node in dag:
        if node not in visited:
            build_topo_from(node)

    return list(reversed(post_order))


def test_topo_order():
    for graph in [g, {"x": [], "y": ["x"], "z": ["y", "x"]}]:
        order = topo_order(graph)
        assert sorted(order) == sorted(graph)
        assert all(order.index(u) < order.index(w) for u in graph for w in graph[u])