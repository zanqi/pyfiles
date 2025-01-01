from collections import deque
from graph_utils import Node, build_graph


"""
DAG BFS.
Node
    val: Number
    neighbors: List<Node>
"""
def bfs_dag(node: Node, target):
    q = deque([node])

    # RI: see bfs()
    while q:
        node = q.popleft()
        if node.val == target:
            return node
        q.extend(node.neighbors)

    # RI: see bfs()
    return None


"""
General BFS handling circle.
Node
    val: Number
    neighbors: List<Node>
"""
def bfs(node: Node, target):
    q = deque([node])
    visited = set()

    # RI: 
    # the nodes in q. 
    # 1. visited contain nodes that have been discovered and processed: 
    #   node.val has been checked != target; 
    #   node.neighbors have been put into q
    # 2. q contains nodes that are discovered but not processed
    # 3. target is not in visited
    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node.val == target:
            return node
        q.extend(node.neighbors)

    # RI: q empty; visited contains all nodes; target not in visited.
    return None

node_vals = [1, 3, 5, 7]
edges = [(0, 1), (1, 2), (2, 3)]
node = build_graph(node_vals, edges)
print(bfs_dag(node, 5))
print(bfs(node, 5))

node_vals = [1]
node = build_graph(node_vals, [])
print(bfs_dag(node, 1))
print(bfs(node, 1))