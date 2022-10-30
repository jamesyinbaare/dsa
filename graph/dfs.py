graph = dict()
graph['A'] = ['B', 'S']
graph['B'] = ['A']
graph['S'] = ['A','G','C']
graph['D'] = ['C']
graph['G'] = ['S','F','H']
graph['H'] = ['G','E']
graph['E'] = ['C','H']
graph['F'] = ['C','G']
graph['C'] = ['D','S','E','F']

def depth_first_search(graph, root):
    visited_virtices = []
    graph_stack = []

    graph_stack.append(root)
    node = root
    while graph_stack:
        if node not in visited_virtices:
            visited_virtices.append(node)
            adj_nodes = graph[node]
            if set(adj_nodes).issubset(set(visited_virtices)):
                graph_stack.pop()
                if len(graph_stack) > 0:
                    node = graph_stack[-1]
                    continue
            else:
                remaining_elements = set(adj_nodes).difference(set(visited_virtices))
                first_adj_node = sorted(remaining_elements)[0]
                graph_stack.append(first_adj_node)
                node = first_adj_node
    return visited_virtices