from collections import deque

graph = dict()
graph['A'] = ['B', 'G', 'D']
graph['B'] = ['A', 'F', 'E']
graph['C'] = ['F', 'H']
graph['D'] = ['F', 'A']
graph['E'] = ['B', 'G']
graph['F'] = ['B', 'D', 'C']
graph['G'] = ['A', 'E']
graph['H'] = ['C']

def breath_first_search(graph, root):
    """BFS """
    visited_vertice = []
    graph_queue = deque([root])
    visited_vertice.append(root)
    node = root

    while len(graph_queue) > 0:
        #print(f"current_queue: {graph_queue}")

        node = graph_queue.popleft()
        adj_nodes = graph[node]
        #print(f"{node}: adjacent_nodes: {adj_nodes}")
        
        remaining_elements = set(adj_nodes).difference(set(visited_vertice))

        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertice.append(elem)
                graph_queue.append(elem)
    
    return visited_vertice




print(breath_first_search(graph, "A"))