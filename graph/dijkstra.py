import heapq

# Passed dijsktra problem on HackerEarth
def dijkstra(graph, initial):
    ''' Dijkstra's shortest path algorithm. '''
    visited = {initial: 0}
    h, path = [(0, initial)], {}
    nodes = set(graph.keys())

    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        while h and (min_node not in nodes):
            current_weight, min_node = heapq.heappop(h)

        nodes.remove(min_node)
        for v, w in graph[min_node]:
            weight = current_weight + w
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                path[v] = min_node
    return visited, path

if __name__ == "__main__":
    g = {
        'b': [('s', 24)],
        's': [('b', 24), ('d', 20), ('c', 3)],
        'c': [('s', 3), ('d', 12)],
        'd': [('s', 20), ('c', 12)]
    }
    print('Graph:')
    for k, vs in g.items():
        print('    {:s}: {:s}'.format(str(k), str(vs)))
    vis, path = dijkstra(g, 's')
    print('Source: s')
    print('Visited:')
    print('    ' + str(vis))
    print('Shortest paths:')
    print('    ' +  str(path))
