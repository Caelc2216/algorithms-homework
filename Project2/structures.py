# Cael Church
# Advanced Algorithms
# 9/11/26

import pytest;


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.parents = {}
        self.edge_list = []
    def add_node(self, node, data=None):
        self.nodes[node] = data

    def add_edge(self, parent, child, data=None):
        if parent not in self.edges:
            self.edges[parent] = {}
        self.edges[parent][child] = data 
        if child not in self.parents:
            self.parents[child] = []
        self.parents[child].append(parent)
        self.edge_list.append((parent, child))

    def add_undirected_edge(self, node1, node2, data=None):
        self.add_edge(node1, node2, data)
        self.add_edge(node2, node1, data)

    def get_node_data(self, node):
        return self.nodes[node]
    
    def get_edge_data(self, parent, child):
        return self.edges[parent][child]

    def get_children(self, parent):
        if parent not in self.edges:
            return []
        return self.edges[parent].keys()

    def get_parents(self, node):
        if node not in self.parents:
            return []
        return self.parents[node]

    def contains_node(self, node):
        if node in self.nodes:
            return True
        else:
            return False

    def contains_edge(self, parent, child):
        if parent in self.edges:
            if child in self.edges[parent]:
                return True
        return False

    def get_nodes(self):
        return self.nodes.keys()

    def get_edges(self):
        return self.edge_list




# Graph Tests
def test_new_graph_has_no_nodes():
    graph = Graph()
    assert list(graph.get_nodes()) == []

def test_add_node_then_contains_node():
    graph = Graph()
    graph.add_node("a")
    assert graph.contains_node("a")
    assert not graph.contains_node("b")

def test_add_node_is_idempotent():
    graph = Graph()
    graph.add_node("a", data=1)
    graph.add_node("a", data=2)  # already present -- should not duplicate
    assert list(graph.get_nodes()) == ["a"]

def test_get_node_data():
    graph = Graph()
    graph.add_node("a", data="hello")
    assert graph.get_node_data("a") == "hello"

def test_add_edge_then_contains_edge():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_edge("a", "b", data=5)
    assert graph.contains_edge("a", "b")
    assert not graph.contains_edge("b", "a")  # directed, so the reverse shouldn't exist

def test_get_edge_data():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_edge("a", "b", data=5)
    assert graph.get_edge_data("a", "b") == 5

def test_add_undirected_edge_creates_both_directions():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_undirected_edge("a", "b", data=7)
    assert graph.contains_edge("a", "b")
    assert graph.contains_edge("b", "a")
    assert graph.get_edge_data("a", "b") == 7
    assert graph.get_edge_data("b", "a") == 7

def test_get_children():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_edge("a", "b")
    graph.add_edge("a", "c")
    assert set(graph.get_children("a")) == {"b", "c"}

def test_get_nodes_preserves_insertion_order():
    graph = Graph()
    graph.add_node("c")
    graph.add_node("a")
    graph.add_node("b")
    assert list(graph.get_nodes()) == ["c", "a", "b"]

def test_get_edges_preserves_insertion_order():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_edge("a", "b")
    graph.add_edge("a", "c")
    assert list(graph.get_edges()) == [("a", "b"), ("a", "c")]

def test_contains_node_false_for_absent_node():
    graph = Graph()
    assert not graph.contains_node("nonexistent")

def test_contains_edge_false_for_absent_edge():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    assert not graph.contains_edge("a", "b")

def test_get_parents_no_parents():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    assert graph.get_parents("a") == []

def test_get_parents_directional():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_edge("a", "b")
    assert graph.get_parents("b") == ["a"]

def test_get_parents_undirectional():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_undirected_edge("a", "b")
    assert graph.get_parents("a") == ["b"]
    assert graph.get_parents("b") == ["a"]



# Priority Queue
class PriorityQueue:
    def __init__(self):
        self.min_queue = []
        self.key = {}

    def update(self, key, priority, data=None, only_if_less=False):
        if key not in self.key:
            self.min_queue.append(key)
            self.key[key] = [data, priority, len(self.min_queue)-1]
        if key in self.key:
            if only_if_less==True:
                if self.key[key][1] > priority:
                    self.key[key][1] = priority
            else:
                self.key[key][1] = priority
        
        currentIndex = self.key[key][2]
        parent_index = (currentIndex - 1)//2
        went_up = False
        went_down = False
        if parent_index >= 0 and parent_index < len(self.min_queue):
            while parent_index >= 0 and self.key[key][1] < self.key[self.min_queue[parent_index]][1]:
                self.min_queue[currentIndex], self.min_queue[parent_index] = self.min_queue[parent_index], self.min_queue[currentIndex]
                currentIndex, parent_index = parent_index, currentIndex
                self.key[key][2] = currentIndex
                self.key[self.min_queue[parent_index]][2] = parent_index
                parent_index = (currentIndex - 1)//2
                went_up = True
        if went_up == False:
            child1_index = (2*currentIndex + 1)
            child2_index = (2*currentIndex + 2)
            if (child1_index >= 0 and child1_index < len(self.min_queue)) or  (child2_index >= 0 and child2_index < len(self.min_queue)):
                while (child1_index < len(self.min_queue) and self.key[key][1] > self.key[self.min_queue[child1_index]][1]) or (child2_index < len(self.min_queue) and self.key[key][1] > self.key[self.min_queue[child2_index]][1]):
                    if child1_index >= len(self.min_queue):
                        c_index = child2_index
                    elif child2_index >= len(self.min_queue):
                        c_index = child1_index
                    elif self.key[self.min_queue[child1_index]][1] < self.key[self.min_queue[child2_index]][1]:
                        c_index = child1_index
                    else:
                        c_index = child2_index
                    self.min_queue[currentIndex], self.min_queue[c_index] = self.min_queue[c_index], self.min_queue[currentIndex]
                    currentIndex, c_index = c_index, currentIndex
                    self.key[key][2] = currentIndex
                    self.key[self.min_queue[c_index]][2] = c_index
                    child1_index = (2*currentIndex + 1)
                    child2_index = (2*currentIndex + 2)

    def peek_min(self):
        return self.min_queue[0]

    def remove(self, key):
        update = self.key[key][2]
        last_index = len(self.min_queue) - 1
        if update != last_index:
            self.min_queue[update], self.min_queue[last_index] = self.min_queue[last_index], self.min_queue[update]
            self.key[self.min_queue[update]][2] = update
            self.min_queue.pop()
            self.update(self.min_queue[update], self.key[self.min_queue[update]][1], None, True)
        else:
            self.min_queue.pop()
        del self.key[key]

    def contains_key(self, key):
        if key in self.key:
            return True
        else: 
            return False
    
    def get_data(self, key):
        return self.key[key][0]

    def get_priority(self, key):
        return self.key[key][1]

    def count(self):
        return len(self.min_queue)



    

# Priority Queue Tests
def test_new_priority_queue_has_count_zero():
    pq = PriorityQueue()
    assert pq.count() == 0

def test_update_adds_new_key():
    pq = PriorityQueue()
    pq.update("a", 5)
    assert pq.count() == 1
    assert pq.contains_key("a")

def test_peek_min_returns_smallest_priority_key():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 2)
    pq.update("c", 9)
    assert pq.peek_min() == "b"

def test_peek_min_does_not_remove():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.peek_min()
    assert pq.count() == 1
    assert pq.contains_key("a")

def test_get_data_returns_associated_data():
    pq = PriorityQueue()
    pq.update("a", 5, data="hello")
    assert pq.get_data("a") == "hello"

def test_update_existing_key_changes_priority_without_duplicating():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 1)
    pq.update("a", 0)  # "a" should now be the minimum
    assert pq.peek_min() == "a"
    assert pq.count() == 2  # still just two keys, not duplicated

def test_update_only_if_less_ignores_higher_priority():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("a", 10, only_if_less=True)  # 10 is not less than 5 -- should be ignored
    pq.update("b", 7)
    assert pq.peek_min() == "a"  # "a"'s priority should still be 5, which beats 7

def test_update_only_if_less_applies_lower_priority():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 3)
    pq.update("a", 1, only_if_less=True)  # 1 is less than 5 -- should apply
    assert pq.peek_min() == "a"

def test_update_only_if_less_on_new_key_still_adds_it():
    pq = PriorityQueue()
    pq.update("a", 5, only_if_less=True)  # "a" wasn't present yet -- should still be added
    assert pq.contains_key("a")
    assert pq.count() == 1

def test_remove_deletes_key():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 2)
    pq.remove("b")
    assert not pq.contains_key("b")
    assert pq.count() == 1
    assert pq.peek_min() == "a"

def test_remove_then_reinsert():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.remove("a")
    pq.update("a", 1)
    assert pq.contains_key("a")
    assert pq.peek_min() == "a"

def test_contains_key_false_for_absent_key():
    pq = PriorityQueue()
    assert not pq.contains_key("nonexistent")

def test_many_updates_and_removes_maintain_min_heap_order():
    pq = PriorityQueue()
    for key, priority in [("a", 5), ("b", 2), ("c", 8), ("d", 1), ("e", 9), ("f", 3)]:
        pq.update(key, priority)
    order = []
    while pq.count() > 0:
        m = pq.peek_min()
        order.append(m)
        pq.remove(m)
    assert order == ["d", "b", "f", "a", "c", "e"]

def test_get_priority():
    pq = PriorityQueue()
    pq.update("a", 6)
    pq.update("b", 8)
    pq.update("c", 69089809)
    pq.update("d", 0)
    assert pq.get_priority("a") == 6
    assert pq.get_priority("b") == 8
    assert pq.get_priority("c") == 69089809
    assert pq.get_priority("d") == 0

def test_get_priority_after_update():
    pq = PriorityQueue()
    pq.update("a", 6)
    pq.update("a", 10, None, False)
    assert pq.get_priority("a") == 10


def prim_mst(graph, edge_weight=None, start_node=None):
    """
    Find minimum spanning tree using Prim's algorithm.
    
    Args:
        graph: an instance of your Graph data structure
        start_node: the node to start from; if None, uses first node from graph.get_nodes()
        edge_weight: function taking (parent, child) returning edge weight;
                     if None, uses edge data as weight
    
    Returns:
        Graph instance containing the minimum spanning tree
    """
    if edge_weight is None:
        edge_weight = lambda parent, child: graph.get_edge_data(parent, child)
    
    if start_node is None:
        start_node = next(iter(graph.get_nodes()))
    
    mst = Graph()  # assuming your Graph class is named Graph
    pq = PriorityQueue()  # assuming your PriorityQueue class is named PriorityQueue
    
    pq.update(start_node, 0, data=None)
    
    while pq.count() > 0:
        current_node = pq.peek_min()
        parent_node = pq.get_data(current_node)
        pq.remove(current_node)
        
        if not mst.contains_node(current_node):
            mst.add_node(current_node)
            if parent_node is not None:
                data = graph.get_edge_data(parent_node, current_node)
                mst.add_undirected_edge(parent_node, current_node, data=data)
            
            for child in graph.get_children(current_node):
                if not mst.contains_node(child):
                    weight = edge_weight(current_node, child)
                    pq.update(child, weight, data=current_node, only_if_less=True)
    
    return mst

def test_prim_mst_basic():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_node("d")
    graph.add_node("e")

    graph.add_undirected_edge("a", "b", 1)
    graph.add_undirected_edge("b", "c", 2)
    graph.add_undirected_edge("c", "d", 3)
    graph.add_undirected_edge("d", "e", 4)


    mst = prim_mst(graph, start_node="b")

    assert mst.contains_edge("a", "b")
    assert mst.contains_edge("b", "c")
    assert mst.contains_edge("c", "d")
    assert mst.contains_edge("d", "e")

    assert mst.get_nodes() == {"b", "a", "c", "d", "e"}

def test_prim_mst_gets_rid_of_cycles():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_node("d")
    graph.add_node("e")

    graph.add_undirected_edge("a", "b", 1)
    graph.add_undirected_edge("b", "c", 2)
    graph.add_undirected_edge("c", "d", 3)
    graph.add_undirected_edge("d", "e", 4)
    graph.add_undirected_edge("e", "a", 6)
    graph.add_undirected_edge("d", "a", 7)
    graph.add_undirected_edge("c", "a", 8)

    mst = prim_mst(graph, start_node="e")

    assert mst.contains_edge("b", "c")
    assert mst.contains_edge("e", "d")
    assert mst.contains_edge("d", "c")
    assert mst.contains_edge("e", "a")

    assert mst.get_nodes() == {"e", "d", "c", "b", "a"}


def test_prim_mst_basic_directed_edges():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_node("d")
    graph.add_node("e")

    graph.add_edge("a", "b", 1)
    graph.add_edge("b", "c", 2)
    graph.add_edge("c", "d", 3)
    graph.add_edge("d", "e", 4)


    mst = prim_mst(graph, start_node="b")

    assert mst.contains_edge("b", "c")
    assert mst.contains_edge("c", "d")
    assert mst.contains_edge("d", "e")

    assert mst.get_nodes() == {"b", "c", "d", "e"}

def test_prim_mst_gets_rid_of_cycles_directed_edges():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_node("d")
    graph.add_node("e")

    graph.add_edge("a", "b", 1)
    graph.add_edge("b", "c", 2)
    graph.add_edge("c", "d", 3)
    graph.add_edge("d", "e", 4)
    graph.add_edge("e", "a", 6)
    graph.add_edge("d", "a", 7)
    graph.add_edge("c", "a", 8)

    mst = prim_mst(graph, start_node="e")

    assert mst.contains_edge("e", "a")
    assert mst.contains_edge("a", "b")
    assert mst.contains_edge("b", "c")
    assert mst.contains_edge("c", "d")

    assert mst.get_nodes() == {"e", "a", "b", "c", "d"}