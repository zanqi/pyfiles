from graph_utils import Node, build_graph


# DAG DFS
# Node
#   val: Number
#   neighbors: List<Node>
# RI:
# 1. node.val has not been checked against target
# 2. dfs return the node within the subgraph that has val == target
def dfs_dag(node: Node, target):
    if node.val == target:
        return node
    for c in node.neighbors:
        found = dfs_dag(c, target)
        if found:
            return found

    # RI: node.val != target; dfs() return None for all node.neighbors
    return None


# General DFS handling circle.
# RI:
# 1. visited contains nodes that are processed: 
#   node.val has been checked != target
# 2. node.val is not checked yet
# 3. return the node within the subgraph that has val == target
def dfs(node: Node, target, visited: set = set()):
    if node.val == target:
        return node
    visited.add(node)
    for c in node.neighbors:
        if c in visited:
            continue
        found = dfs(c, target, visited)
        if found:
            return found
    # RI: node.val != target; dfs() return None for all node.neighbors
    return None


node_vals = [1, 3, 5, 7]
edges = [(0, 1), (1, 2), (2, 3)]
node = build_graph(node_vals, edges)
print(dfs_dag(node, 5))
print(dfs(node, 5))
