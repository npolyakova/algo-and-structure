class Graph:
    def __init__(self):
        self.graph = {}

    # добавляем ребро между вершинами u и v или добавляем сначала саму вершину, если ее не было
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    # принимает конкретную вершину и возвращает кратчайший путь
    def execute_bford_algorythm(self, source):
        dist = {vertex: float('inf') for vertex in self.graph}
        dist[source] = 0

        for i in range(len(self.graph)):
            for u in dist:
                for v, weight in self.graph[u]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight

        negative_cycle = False
        for u in self.graph:
            for v, weight in self.graph[u]:
                if dist[u] + weight < dist[v]:
                    negative_cycle = True
                    break
            if negative_cycle:
                break

        return dist if not negative_cycle else None

if __name__ == '__main__':
    cities_graph = Graph()
    cities_graph.add_edge('Москва', 'Санкт-Петербург', 7)
    cities_graph.add_edge('Санкт-Петербург', 'Выборг', 3)
    #cities_graph.add_edge('Санкт-Петербург', 'Рускеала', 4)
    cities_graph.add_edge('Выборг', 'Рускеала', 4)
    cities_graph.add_edge('Рускеала', 'Москва', 10)
    source = 'Москва'
    print(cities_graph.execute_bford_algorythm(source))