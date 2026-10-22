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

# Part 2
# 1. This is slow, it takes at least O(n log n) to sort a list and if you do that n-1 times it is O(n^2 log n)
# 2. This can be slow, quickselects worst case is n^2 because if pivots are chosen poorly you have to go over every item in the list comparing it with every item in the list, and if you do that at every step it becomes worst case of O(n^3)
# 3. This is wrong, it is not always the case that the merge of the two smallest still is part of the next 2 smallest. An example is the one given in part 1 with (a, 3), (b, 8), (c, 10), (d, 14), (e, 17), (f, 42). They are already in sorted order, if we start by combining a and b the total weight = 11. Next we combine it with c which gives a weight of 21, but now the next two that should be combined are d and e, instead our algorithm would merge d in to a, b, c. This would lead the total cost to be 213. Hereas the cost of the Huffman tree is 209

# Part 3
# 1. To store the tree you only need to store each node once O(n) using a nested tuple or some other data structure. Whereas to store the bit strings each level you go down in the tree adds another bit that you need to store, this creates a worst case with a depth of O(n) so a space complexity of O(n^2). So storing the nodes in a data structure better optimizes the space complexity
import random

class Codec():
    def __init__(self, graph: Graph, map, root):
        self.graph = graph
        self.map = map
        self.root = root

    def encode(self, symbols):
        encoded_message = []
        for s in symbols:
            node = self.map[s]
            bit_string_reversed = []
            current_node = node
            if (current_node is self.root and self.root in self.map):
                bit_string_reversed.append(0)
            while (current_node is not self.root):
                bit_string_reversed.append(self.graph.get_node_data(current_node))
                current_node = self.graph.get_parents(current_node)[0]
            encoded_message.extend(list(reversed(bit_string_reversed)))
        return encoded_message

    def decode(self, coded_message):
        current_node = self.root
        for bit in coded_message:
            if (len(list(self.graph.get_children(current_node))) == 0 and self.root in self.map):
                yield self.root
            else:
                children = list(self.graph.get_children(current_node))
                child1_data = self.graph.get_node_data(children[0])
                child2_data = self.graph.get_node_data(children[1])
                if child1_data == bit:
                    current_node = children[0]
                elif child2_data == bit:
                    current_node = children[1]
                if (len(list(self.graph.get_children(current_node))) == 0):
                    yield current_node
                    current_node = self.root
            
            
def huffman_codec(frequencies):
    queue = PriorityQueue()
    graph = Graph()
    if(len(frequencies) == 0):
        return Codec(graph, {}, None)
    for node in frequencies:
        queue.update(node[0], node[1])

    if (queue.count()) == 1:
        graph.add_node(frequencies[0])
    for _ in range(queue.count() - 1):
            
        node1 = queue.peek_min()
        node1_priority = queue.get_priority(node1)
        queue.remove(node1)
        node2 = queue.peek_min()
        node2_priority = queue.get_priority(node2)
        queue.remove(node2)
        parent = random.Random()

        graph.add_node(node1, 0)
        graph.add_node(node2, 1)
        graph.add_node(parent)
        graph.add_edge(parent, node1)
        graph.add_edge(parent, node2)

        queue.update(parent, node1_priority + node2_priority)

    map = {}
    # I designed the tree so that the leaf nodes are the symbols, so the map[symbol] = symbol
    for n in frequencies:
        map[n[0]] = n[0]

    
    return Codec(graph, map, queue.peek_min())
