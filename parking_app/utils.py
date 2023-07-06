from collections import defaultdict
import heapq

def calculate_shortest_distance(graph, root):
    distances = defaultdict(lambda: float('inf'))
    distances[root] = 0
    pq = [(0, root)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue

        for neighbor, edge_weight in graph[node].items():
            new_distance = distances[node] + edge_weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances
