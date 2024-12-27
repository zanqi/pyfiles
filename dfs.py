def dfs(node, target):
    # RI: if target is in the graph, it is reachable from node
    if not node or node.val == target:
        return node
    for c in node.neighbors:
        found = dfs(c, target)
        if found:
            return found
    
    # RI: no neighbors of node can reach target
    return None


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
def create_graph(node_vals, edges):
    nodes = [Node(v) for v in node_vals]
    for i, j in edges:
        nodes[i].neighbors.append(nodes[j])
    return nodes[0]

node_vals = [1, 3, 5, 7]
edges = [(0, 1), (1, 2), (2, 3)]
node = create_graph(node_vals, edges)
print(dfs(node, 5))