'''
Create a program that finds the shortest path
through a graph using its edges.
'''
from pprint import pprint as pp
class Graph(object):
    def __init__(self, edges):
        self.edges    = edges
        self.vertices = set(sum(([e[0], e[1]] for e in edges), []))

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: float('inf') for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))

        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == float('inf') or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:   # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        s, u = [], dest
        while previous[u]:
            s.insert(0, u)
            u = previous[u]
        s.insert(0, u)
        return s


graph = Graph([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
               ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
               ("e", "f", 9)])
pp(graph.dijkstra("a", "e"))