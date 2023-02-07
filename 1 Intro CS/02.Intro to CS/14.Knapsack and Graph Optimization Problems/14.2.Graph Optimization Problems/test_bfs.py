from graph import Node, Edge, Digraph, print_path
from bfs_algorithm import bfs

def test_shortest_path(to_print=False):
    nodes = []
    number_of_nodes = 6
    for name in range(number_of_nodes):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[1], nodes[2]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[0]))
    g.add_edge(Edge(nodes[3], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[0]))
    sp = bfs(g, nodes[0], nodes[5], to_print=to_print)
    print(f'Shortest path found by BFS: {print_path(sp)}')


if __name__ == '__main__':
    test_shortest_path(True)
