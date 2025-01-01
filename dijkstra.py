from heapq import heappop, heappush


def dijkstra(graph, start, end):
    q = [(0, start)]  # distance, node
    visited = set()

    # RI:
    # 1. q contains discovered, but not processed nodes
    # 2. visited contains processed nodes (!= end; neighbors added into q)
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
