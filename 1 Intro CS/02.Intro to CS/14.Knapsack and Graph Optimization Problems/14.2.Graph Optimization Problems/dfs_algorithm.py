from graph import Node, Digraph, print_path


def dfs(graph: Digraph, start: Node, end: Node, path: [Node], shortest: [Node], to_print: bool = False) -> [Node]:
    '''Depth-first-search algorithm'''
    path = path + [start]
    if to_print:
        print(f'Current DFS path: {print_path(path)}')
    if start == end:
        return path
    if graph.len_nodes() < len(path):
        # no way
        return None
    for node in graph.children_of(start):
        # avoid cycles
        if node not in path:
            if shortest is None or len(path) < len(shortest):
                new_path = dfs(graph, node, end, path, shortest, to_print)
                if new_path is not None:
                    shortest = new_path
    return shortest


def shortest_path(graph: Digraph, start: Node, end: Node, to_print: bool = False) -> [Node]:
    '''Depth-first-search shortest-path algorithm'''
    return dfs(graph, start, end, [], None, to_print)
