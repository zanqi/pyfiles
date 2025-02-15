from heapq import heappop, heappush


def dijkstra(graph, start, end):
    q = [(0, start)]  # distance, node
    visited = set()

    # inv:
    # 1. q contains discovered nodes, but neighbors not queued yet.
    # 2. visited nodes' neighbors are queued
    # complexity: E nodes added into q. 
    #     Each iteration has a heappop
    #     Each unvisited node has d heappush.
    #     T(V, E) = Elog(E) + Elog(E) = Elog(E)
    # Compare to dijkstra with decreaseKey: Elog(V). It's the same!
    while q:
        d, node = heappop(q)
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return d
        for c, n in graph[node]:
            heappush(q, (d + c, n))

    # q empty: all discovered and processed. end not found.
    return -1


graph = {"A": [(1, "B"), (1, "C"), (1, "D")], "B": [(1, "D")], "C": [(1, "D")], "D": []}
print(dijkstra(graph, "A", "C"))
print(dijkstra(graph, "A", "D"))
print(dijkstra(graph, "B", "A"))
