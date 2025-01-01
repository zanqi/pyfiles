class Node(object):
    def __init__(self, v):
        self.val = v
        self.neighbors = []
    
    def __repr__(self):
        return f'val: {self.val}, neighbors: {self.neighbors}'

"""
Nodes are numbered from 0 to len(node_vals).
Node 0 is the starting node. Pass it to graph algorithm.
Example:
    node_vals = [1, 3, 5, 7]
    edges = [(0, 1), (1, 2), (2, 3)]
    node = create_graph(node_vals, edges)
    print(dfs(node, 5))
"""
def build_graph(node_vals, edges):
    nodes = [Node(v) for v in node_vals]
    for i, j in edges:
        nodes[i].neighbors.append(nodes[j])
    return nodes[0]