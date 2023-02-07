class Node(object):
    def __init__(self, name: str):
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name


class Edge(object):
    def __init__(self, source: Node, destination: Node):
        self._source = source
        self._destination = destination

    def get_source(self):
        return self._source

    def get_destination(self):
        return self._destination

    def __str__(self):
        return f'{self._source.get_name()} -> {self._destination.get_name()}'


class WeightedEdge(Edge):
    def __init__(self, source: Node, destination: Node, weight=1.0):
        super().__init__(source, destination)
        self._weight = weight

    def get_weight(self):
        return self._weight

    def __lt__(self, other):
        return self._weight < other

    def __str__(self):
        return f'{self._source.get_name()} ->({self._weight}) {self._destination.get_name()}'


class Digraph(object):
    # nodes is a list of the nodes in the graph
    # edges is a dict mapping each node to a list of its children
    def __init__(self):
        self._nodes = []
        self._edges = {}

    def add_node(self, node):
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []

    def add_edge(self, edge):
        source = edge.get_source()
        destination = edge.get_destination()
        if not (source in self._nodes and destination in self._nodes):
            raise ValueError('Node not in graph')
        self._edges[source].append(destination)

    def children_of(self, node):
        return self._edges[node]

    def has_node(self, node):
        return node in self._nodes

    def get_edges(self):
        return self._edges

    def len_nodes(self):
        return len(self._nodes)

    def __str__(self):
        result = ''
        for source in self._nodes:
            for destination in self._edges[source]:
                result += f'{source.get_name()} -> {destination.get_name()}\n'
        return result[:-1]


class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)

def print_path(path: [Node]) -> str:
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += ' -> '
    return result